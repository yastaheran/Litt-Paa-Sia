"""
Choose your favorite way of integrating C with Python. (We recommend
cython.) Make yet another script using that to do the same computations,
and compare the runtime to your previous examples. How much is gained by
switching to C?
In this problem the goal is to make your program more effective.
As such, getting a good score on this problem requires good use of
Cython’s features (or your module of choice) to improve the performance of
your program, so simply taking your existing solution from 4.1 or 4.2 and submitting
it without making any changes will not give you a good score.
"""
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

cpdef mandelbrot3(double xmin, double xmax, double ymin, double ymax):
    cdef:
        double[:] xvalues = numpy.linspace(xmin, xmax, 1000)
        double[:] yvalues = numpy.linspace(ymin, ymax, 1000)
        int[:,:] rectangle = numpy.empty((1000,1000), np.int)
        int i,j
    
    for i in range(1000):
        for j in range(1000):
            rectangle[i,j] = mandel3(xvalues[i], yvalues[j], 40)
     
    return (xvalues,yvalues,rectangle)    