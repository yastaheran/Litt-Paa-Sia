import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')

# Initial function given
def f(x):
    return x**2


# Definite integral of the function from a to b
def F(a,b):
    if a > b:
        raise ValueError('b must be greater than a')
    elif a == b:
        return 0
    else:
        return (b**3-a**3)/3

# rectangular
def miniArea(c,d):
	return (d-c)*f((c+d)/2)

# Approximating function using numerical metod: rectangular
def numpy_integrate(a, b, N=10):
    if N < 2:
        raise ValueError('N must be greater than 2')
    if a == b:
        return 0
        
    n = np.linspace(a, b, N)
    partSum = 0
    
    for i in range(1,len(n)):
        partSum += miniArea(n[i-1],n[i])
    e = (partSum-F(a,b))/F(a,b) *100
    
	print('\nApproximating using rectangular rule...')
	print('Percentage error: ',e,'%')
	plot_dat(a, b, N)
        
    return e

# Plotting function for a visual representation
def plot_dat(a,b,points,mod='rectangular'):

    n = np.linspace(a,b,points)
    plt.plot(n,f(n),color='red')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Numerical approximation')
        
    for i in range(1,len(n)):
		c = n[i-1]
		d = n[i]
		plt.plot([c,c],[0,f((c+d)/2)],color='blue')
		plt.plot([d,d],[0,f(d)],color='blue')
		plt.plot([c,d],[f((c+d)/2),f((c+d)/2)],color='blue')
	plt.show()
    return 0
    
# Approximate area with a given precision
def approxGivenPrecision(a,b,error=0.5,mod='rectangular',printf=False):
    e = 100
    p = 5
    itMax = 500
    it = 0
    while abs(e) > error:
        area,e = approximateNumerical(a,b,mod=mod,points=p)
        p += 10
        it += 1
        if printf:
            print('Approximating using '+mod+' rule with:',p,'points, percentage error:',e,'%')
        if it > itMax:
            print('Number of iterations exceeded: '+str(itMax))
            break
    return area