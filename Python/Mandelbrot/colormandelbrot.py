"""
Use your script to make pretty pictures. Add support for additional color scales
to your script, giving the user at least 3 visually distinct options, and experiment
with different color scales and locations to render, and make up a picture you
think look cool.

Name of your contest submission: contest image.jpg/png/whatever
"""
import matplotlib.pyplot as plt
import numpy as np
import sys
   
def main():
    if sys.argv[1] == '--help':
        print("Syntax: colormandelbrot.py <xmin> <xmax> <ymin> <ymax> <color scale> ")
        print("Color scale names: Pastel1, Ocean, inferno")
    else
        mandelbrot(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])

def mandel(c, maxIterations):
    z = complex(0,0)
    for iteration in range(maxIterations):
        z = (z*z) + c
        if abs(z) > 2:
           return iteration
    return 0 

def mandelbrot(xmin, xmax, ymin, ymax, colorscale):
    xvalues = np.linspace(xmin, xmax, 1000)
    yvalues = np.linspace(ymin, ymax, 1000)
    xlen = len(xvalues)
    ylen = len(yvalues)
    rectangle = np.zeros((xlen,ylen))
    for ix in range(xlen):
        for iy in range(ylen):
            cx = xvalues[ix]
            cy = yvalues[iy]
            c = complex(cx, cy)

            rectangle[ix,iy] = mandel(c, 130)
    
    # make the image and show it
    plt.figure(figsize=(18,18))
    plt.imshow(rectangle.T, cmap=colorscale, interpolation="bicubic")
    plt.savefig("contestimage.png")
    plt.show()

if __name__ = '__main__':
	main()