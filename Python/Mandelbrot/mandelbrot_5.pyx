"""
Provide a command line user interface for your script. The design of this is up
to you, but it should provide instructions for its by calling it with a --help
flag, and it should be possible to specify which region of the plane to draw, the
resolution to draw in and output image filename. It should also be possible to
switch between your 3 implementations with a command line argument. 


This file has not been compiled nor tested.
"""

#!/usr/bin/env python

import numpy
import sys
import matplotlib.pyplot as plt
cimport numpy


def main():
    if sys.argv[1] == '--help':
        print("Choose between:")
        print("mandelbrot_5.pyx <mandelbrot no> <xmin> <xmax> <ymin> <ymax> <resolution> <output image filename>")
        print("mandelbrot_5.pyx <mandelbrot no> <xmin> <xmax> <ymin> <ymax> <resolution> <output image filename>")
        print("mandelbrot_5.pyx <mandelbrot no> <xmin> <xmax> <ymin> <ymax> <resolution> <output image filename>")
    elif sys.argv[1] == '1':
        mandelbrot1(sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6], sys.argv[7]);
    elif sys.argv[1] == '2':
        mandelbrot2(sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6], sys.argv[7]);
    elif sys.argv[1] == '3':
        mandelbrot3(sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6], sys.argv[7]);
    
#oppgave 1
def mandel1(c, maxIterations):
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
    
def mandelbrot1(xmin, xmax, ymin, ymax, res, outputname):
    # Rectangle - the location and size
    xvalues = numpy.linspace(xmin, xmax, 1000)
    yvalues = numpy.linspace(ymin, ymax, 1000)

    # size of these lists of x and y values
    xlen = len(xvalues)
    ylen = len(yvalues)
    
    # create an array of the right size to represent the rectangle
    rectangle = numpy.zeros((xlen,ylen))
    
    # go through each point in this array and test to see how many iterations are needed to diverge (or reach the maximum iterations when not diverging)
    for ix in range(xlen):
        for iy in range(ylen):
            
            # works out what the actual real and imaginary parts of x are by looking it up in the xvalue and yvalue lists
            cx = xvalues[ix]
            cy = yvalues[iy]
            c = complex(cx, cy)

            rectangle[ix,iy] = mandelbrot(c, 40)
    
    # make the image, save & show it
    plt.figure(figsize=(18,18), dpi = res)
    plt.imshow(rectangle.T, cmap ='hot', interpolation="nearest")
    plt.savefig("outputname")
    plt.show()

#oppgave 2
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
    
def mandelbrot2(xmin, xmax, ymin, ymax, res, outputname):
    # Rectangle location, datatype and size    
    xvalues = np.linspace(xmin, xmax, 1000, dtype=np.float32)
    yvalues = np.linspace(ymin, ymax, 1000, dtype=np.float32)   
    
    c = xvalues + yvalues[:,None]*1j    
    rectangle = mandel2(c, 40)    
    
    # make the image, save & show it
    plt.figure(figsize=(18,18), dpi = res)
    plt.imshow(rectangle.T, interpolation="nearest")
    plt.savefig(outputname)
    plt.show()

    return(xvalues,yvalues,rectangle.T)
    
#oppgave 3
    
#!/usr/bin/env cython
import numpy
cimport numpy

cdef int mandel3(double creal, double cimag, int mi):
    cdef:
        double real2, imag2
        double real = creal, imag = cimag
        int it

    for it in range(mi):
        # generates the output value of z
        real2 = real*real
        imag2 = imag*imag
        
        # check if the output complex number z is bigger than 2
        if real2 + imag2 > 2.0:
            return it
            
        imag = 2* real*imag + cimag
        real = real2 - imag2 + creal;
    return 0
    
# Cython is free to assume that indexing operations in the code will not cause any IndexErrors to be raised.
@cython.boundscheck(False) 
#Cython will not ensure that python indexing is not used
@cython.wraparound(False)

cpdef mandelbrot3(double xmin, double xmax, double ymin, double ymax, int res, String outputname):
    cdef:
        double[:] xvalues = numpy.linspace(xmin, xmax, 1000)
        double[:] yvalues = numpy.linspace(ymin, ymax, 1000)
        int[:,:] rectangle = numpy.empty((1000,1000), numpy.int)
        int i,j
    
    for i in range(1000):
        for j in range(1000):
            rectangle[i,j] = mandel3(xvalues[i], yvalues[j], 40)
    
     # make the image, save & show it
    plt.figure(figsize=(18,18), dpi = res)
    plt.imshow(rectangle.T, interpolation="nearest")
    plt.savefig(outputname)
    plt.show()
    
    return (xvalues,yvalues,rectangle)    

if __name__ == "__main__":
    main()