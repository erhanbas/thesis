import scipy as sp
import numpy as np
import scipy.optimize
import matplotlib.pyplot

def henon(init, args):
    """
    args = (a,b)
    init = (x0, y0)
    Henon map 
    f(x,y) = y + 1 - ax^n
    g(x,y) = b*x
    """
    a = args[0]
    b = args[1]
    x0 = init[0]
    y0 = init[1]
    x = y0 + 1 - a*(x0**2)
    y = b * x0
    return (x,y)

def roessler(init, args):
    pass

def IterateList2D(g, init, N, args=()):
    """
    Iterate the function g(x, mu) N-1 times, starting at x0, so that the
    full trajectory contains N points.
    Returns the entire list 
    (x, g(x), g(g(x)), ... g(g(...(g(x))...))). 

    use
        pylab.hist(attractorXs, bins=500, normed=1)
        pylab.show()
    to see the density of points.
    """
    x0 = init[0]
    y0 = init[1]

    result = [(x0, y0)]
    for i in range(N-1):
      result.append(g(result[-1],args))

    # Return a numpy array
    return np.array(result)

def PlotIterate2D(g, init, N, args=()):
    """
    Plots g, the diagonal y=x, and the boxes made of the segments
    [[x0,x0], [x0, g(x0)], [g(x0), g(x0)], [g(x0), g(g(x0))], ...
    """
    points = IterateList2D(g, init, N, args)
    matplotlib.pyplot.scatter(points[:,0], points[:,1], s=0.1, color='darkblue')