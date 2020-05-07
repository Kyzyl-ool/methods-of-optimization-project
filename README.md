# methods-of-optimization-project
 Stochastic Cubic Regularization for Fast Nonconvex Optimization

# Abstract

This paper proposes a stochastic variant of a classic algorithm—the cubicregularized Newton method. The proposed algorithm efficiently escapes saddle points and finds approximate local minima for general smooth, nonconvex functions in only O(e^ -3.5) stochastic gradient and stochastic Hessian-vector product evaluations. The latter can be computed as efficiently as stochastic gradients. This improves upon the O(e^-4) rate of stochastic gradient descent. Our rate matches the best-known result for finding local minima without requiring any delicate acceleration or variance-reduction techniques.

# Introduction 

We consider the problem of nonconvex optimization in the stochastic approximation framework

