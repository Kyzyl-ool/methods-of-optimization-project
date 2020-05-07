# methods-of-optimization-project
 Stochastic Cubic Regularization for Fast Nonconvex Optimization

# Abstract

This paper proposes a stochastic variant of a classic algorithm—the cubicregularized Newton method. The proposed algorithm efficiently escapes saddle points and finds approximate local minima for general smooth, nonconvex functions in only O(e^ -3.5) stochastic gradient and stochastic Hessian-vector product evaluations. The latter can be computed as efficiently as stochastic gradients. This improves upon the O(e^-4) rate of stochastic gradient descent. Our rate matches the best-known result for finding local minima without requiring any delicate acceleration or variance-reduction techniques.

# Introduction 

We consider the problem of nonconvex optimization in the stochastic approximation framework
 - q2.png
In this setting, we only have access to the stochastic function f(x;e), where the random variable e is sampled from an underlying distribution D. 

The task is to optimize the expected function f(x), which in general may be nonconvex.

 One of the most prominent applications of stochastic optimization is the optimization of deep
neural networks.

A local minimum is defined as a point x satisfying - q3.png and - q4.png

stochastic gradient descent (SGD) is the best  (simplest and most versatile) for finding local minimum which needs s O(e^-4 poly(d)) iterations

(среди вторых порядков расширениие градспуска -)The cubic-regularized Newton method of Nesterov and Polyak finds the minimizer of a local second-order Taylor expansion at each step,
- q6.png
the cubic regularized Newton method finds the minimizer of a local third-order Taylor expansion,
- q7.png

# Most previous work on the cubic-regularized Newton method has focused on the non-stochastic orpartially-stochastic settings. This leads us to ask the central questions of this paper: Can we design a fully stochastic variant of the cubic-regularized Newton method? If so, is such an algorithm faster than SGD?

# In this work, we answer both questions in the affirmative, bridging the gap between its use in the non-stochastic and stochastic settings.

We provide algorithm finds an e-second-order stationary point using only O(e^-3.5) stochastic gradient and stochastic Hessian-vector
evaluations, where O(·) hides poly-logarithmic factors.

# Improve upon O(e^-4) rate of SGD (без всякой мелкой суеты)
# Works on both synthetic and real non-convex problems

(1.1.1 s. However, these algorithms rely on having access to the full Hessian at each iteration, which is
prohibitive in high dimensions.)

gradient descent solver для подзадач позволяет нах стац точку второго порядка за O(e^-2) также можно апгрейдить до O(e^-1.75)
- q9.png



We are interested in stochastic optimization problems of the form minx2Rd f(x) := E⇠⇠D[f(x; ⇠)],
where ⇠ is a random variable with distribution D. In general, the function f(x) may be nonconvex.
This formulation covers both the standard offline setting where the objective function can be expressed
as a finite sum of n individual functions f(x, ⇠i), as well as the online setting where data arrives
sequentially.
# Our goal is to minimize the function f(x) using only stochastic gradients rf(x; ⇠) and stochastic Hessian-vector products r2f(x; ⇠) · v, where v is a vector of our choosing.

f(x) ограничена f* и вып след гладкость:
- q10.png
делаем след преположение
- q11.png  (можно и др условия ) 


# 2.2 Cubic Regularization

- q12.png
the cubic submodel:
- q13.png

три проблемы 
