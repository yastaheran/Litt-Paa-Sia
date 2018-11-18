"""
Make your implementation into a Python module or package and make a setup
script. Your package should include a method compute mandelbrot(xmin,
xmax, ymin, ymax, Nx, Ny, max escape time=1000, plot filename=None)
which returns an Nx × Ny array of the escape times of evenly sampled points
in the rectangle [xmin, xmax] × [ymin, ymax]. If plot filename is supplied,
an image should be rendered and saved to the specified location. You are free
to make other methods which you think add useful functionality.
Further, make two unit tests. One should test that if you choose a region
of the plane which is entirely outside the Mandelbrot set after 0 iterations (like
the rectangle [3, 4] × [3, 4]), your script notices. Another should check that if
you take a region which is entirely inside the Mandelbrot set, your script should
not say they are outside. You are free to choose which unit testing framework
to use for writing your tests, provided it is reasonably standard. py.test is a
good option.
"""
"""
Not finnished
"""

def compute_mandelbrot(xmin,xmax, ymin, ymax, Nx, Ny, max_escape_time=1000, plot_filename=None):