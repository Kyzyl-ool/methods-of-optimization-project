#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 18 20:51:29 2020

@author: kyzyl-ool
"""


import torch
import math
from torch.optim.optimizer import Optimizer
from torch.nn import Module
from copy import deepcopy


class CubicNewton(Optimizer):
    
    
    """Implements Cubic Newton Method with gradient descent as a subsolver.


    Arguments:
        params (iterable): iterable of parameters to optimize or dicts defining
            parameter groups
        lr (float, optional): learning rate of the gradient descent (default: 1e-1)
        L (float, optional): Lipshitz constant of the Hessian (default: 1e+1)
        eps (float, optional): Desired accuracy for the norm of the model's gradient, used for the stopping criterion  (default: 1e-4)
        max_itet (integer, optional): maximal number of inner iterations of the gradient descent to solve subproblem (default: 10)

    """

    def __init__(self, params, output=None, L = 1e+1, lr = 1e-1, eps = 1e-4, max_iter = 10):
        if not 0.0 <= lr:
            raise ValueError("Invalid learning rate: {}".format(lr))
        if output == None:
            raise ValueError("Invalid output: {}".format(output))

        defaults = dict(output = output, L = L, lr = lr, eps = eps, max_iter = max_iter)
        super(CubicNewton, self).__init__(params, defaults)

        for group in self.param_groups:
            for p in group['params']:
                state = self.state[p]
                state['step'] = 0.
                state['ak'] = 0.
  

    def share_memory(self):
        for group in self.param_groups:
            for p in group['params']:
                state = self.state[p]
                state['ak'].share_memory_()
                
    
    def step(self, closure=None):
        """Performs a single optimization step.

        Arguments:
            closure (callable, optional): A closure that reevaluates the model
                and returns the loss.
        """
        for group in self.param_groups:
            params = group['params']
            output = group['output']
            lr = group['lr']
            L = group['L']
            max_iter = group['max_iter']
            
            
            #Gradient computation
            grads = torch.autograd.grad(output, list(params), create_graph = True)
            
            #Zero step of gradient descent
            v = []
            for i in range(len(grads)):
                v.append(torch.neg(grads[i]).mul(lr))
                
                
                
            #Computation cycle that solve subproblem by gradient descent
            j = 0
            while (j < max_iter-1):
                
                grads = torch.autograd.grad(output, list(params), create_graph = True)
                #Hessian-vector product
                dot = 0
                norm = 0
                for i in range(len(grads)):
                    norm += v[i].square().sum()  #Computing ||v||_2^2
                    dot += grads[i].mul(v[i]).sum()
                hvp = torch.autograd.grad(dot, list(params), retain_graph = True)
                
                norm = math.sqrt(norm) #Computing ||v||_2
                
                
                model_gradient_norm = 0
                for i in range(len(grads)):
                    #Gradient of the model for gradient steps, used for the stoping criterion
                    model_gradient = grads[i]+hvp[i]+v[i].mul(norm * L / 2) 
                    model_gradient_norm += model_gradient.square().sum()
                    #Gradient step with h = lr
                    v[i].sub_(model_gradient, alpha = lr)
                    
                    
                if model_gradient_norm <= eps**2:
                        j = max_iter
            
                
            
            #Full step update of parameters
            with torch.no_grad():
                for i in range(len(grads)):
                    list(params)[i].add_(v[i])
                

        return None
        

    #not used, but show how we compute Hessian-vector product            
    def hessian_vec_prod(output, params, vector):
        grads = torch.autograd.grad(output, params, create_graph = True)
        dot = 0
        for i in range(len(grads)):
            dot += grads[i].mul(vector[i]).sum()
        hvp = torch.autograd.grad(dot, params, retain_graph = True)
        return hvp
    
    

   
    
