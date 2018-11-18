"""
Make a similar script to 4.1 so that all computationally heavy bits use numpy
arrays. Compare the runtime on some input of your choosing. How much is
gained by switching to numpy?
"""
#!/usr/bin/env python

import numpy as np
import time
import matplotlib.pyplot as plt
    
# takes the fixed parameter c and the maximum number of iterations as inputs
def mandel2(c, maxIterations):
    output = np.zeros(c.shape)
    
    # Start value of complex z
    z = np.zeros(c.shape, np.complex64)
    
    # start iterating and stop when maxIterations
    for iteration in range(maxIterations):
        # check if the output complex number z is bigger than 2, if so save in notdone
        notdone = np.less(z.real*z.real + z.imag*z.imag, 2.0)
        
        # assignes iteration to alle the elements of output where where the corresponding of notdone is True
        output[notdone] = iteration
        
        # generates the output value of z
        z[notdone] = z[notdone]**2 + c[notdone]
    output[output == maxIterations-1] = 0
    return output
    
def mandelbrot2(xmin, xmax, ymin, ymax):
    # Rectangle location, datatype and size    
    xvalues = np.linspace(xmin, xmax, 1000, dtype=np.float32)
    yvalues = np.linspace(ymin, ymax, 1000, dtype=np.float32)   
    
    t0 =  time.time()
    c = xvalues + yvalues[:,None]*1j    
    rectangle = mandel2(c, 1000)    
    t1 = time.time()
    print("Runtime mandelbro: {}".format(t1-t0))


    # make the image & show it
    plt.figure(figsize=(18,18))
    plt.imshow(rectangle.T, interpolation="nearest")
    plt.savefig("mandelbrot2.png")
    plt.show()

    return(xvalues,yvalues,rectangle.T)
    
mandelbrot2(-2.0, 0.5, -1.25, 1.25)