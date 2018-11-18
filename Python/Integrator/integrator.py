#!/usr/bin/env python
import matplotlib.pyplot as plt

# the function to be integrated
def func(x):
	return x*x;

#check if b is greater than a	
def ab(a, b):
	if a == b:
        return 0
    else:
        return (b**3-a**3)/3

def integrate(f, a, b, N):
	if ab(a, b):
		#define the variable for area
		area = 0
	
		#loop to calculate the area of each trapezoid and sum
	#	for i in range(1, N+1):
			#the x locations of the left and right side of each trapezpoid
			x0 = a+(i-1)*dx
			x1 = a+i*dx
		
			#the area of each trapezoid
			ai = dx * (func(x0) + func(x1))/ 2.

    		# cumulatively sum the areas
    		area = area + ai

		#print out the result.
		print "Area = ", area
		plot_data()
	else:
		raise ValueError('b must be greater than a')

#visual representation of integral
def plot_data(a, b, N):
	
	plt.plot(n, f(n), color = 'red')
	plt.xlabel('x')
	plt.ylabel('y')
	plt.title('Numerical integrate')
	
	for i in range(1, len(n))
		c = n[i-1]
		d =n[i]
		plt.plot([c,c],[0,f((c+d)/2)],color='blue')
		plt.plot([d,d],[0,f(d)],color='blue')
		plt.plot([c,d],[f((c+d)/2),f((c+d)/2)],color='blue')
	
	plt.figure(figsize=(18,18))
    plt.imshow(rectangle.T, cmap=colorscale, interpolation="bicubic")
    plt.savefig("quadratic_error.png")
	plt.show()
	return 0