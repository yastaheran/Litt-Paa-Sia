#!/usr/bin/env python

import numpy
import matplotlib.pyplot as plt
import time 

# takes the fixed parameter c and the maximum number of iterations as inputs
def mandelbrot(c, maxIterations):
    # starting value of complex z is 0+0i
    z = complex(0,0)
    
    # start iterating and stop when maxIterations
    for iteration in range(maxIterations):
        
        # generates the output value of z
        z = (z*z) + c
        
        # check if the output complex number z is bigger than 2, if so stop iterating
        if abs(z) > 2:
           return iteration
        
    return 0  
    
def mandelsize(xmin, xmax, ymin, ymax):
    # Rectangle - the location and size
    xvalues = numpy.linspace(xmin, xmax, 1000)
    yvalues = numpy.linspace(ymin, ymax, 1000)

    # size of these lists of x and y values
    xlen = len(xvalues)
    ylen = len(yvalues)
    
    # create an array of the right size to represent the rectangle
    rectangle = numpy.zeros((xlen,ylen))
      
   # t0 = time.time()
    # go through each point in this array and test to see how many iterations are needed to diverge (or reach the maximum iterations when not diverging)
    for ix in range(xlen):
        for iy in range(ylen):
            
            # works out what the actual real and imaginary parts of x are by looking it up in the xvalue and yvalue lists
            cx = xvalues[ix]
            cy = yvalues[iy]
            c = complex(cx, cy)

            rectangle[ix,iy] = mandelbrot(c, 1000)
   # t1 = time.time()
   # print("Runtime mandelbrot: {}".format(t1-t0))

    # make the image & show it 
    plt.figure(figsize=(18,18))
    plt.imshow(rectangle.T, interpolation="nearest")
    plt.savefig("mandelbrot2.png", dpi=plt.figure)
    plt.show()

mandelsize(-2.0, 0.5, -1.25, 1.25)