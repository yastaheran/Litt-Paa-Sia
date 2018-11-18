#!/usr/bin/env python

class Polynomial:
	
	#changes the order of coefficients
	@property
	def order(self):
		for i in range(len(self.coefficients)-1,-1,-1):
			if self.coefficients[i] != 0:
				return i
		return 0
	
	def __getitem__(self, items):
		if isinstance(items, int):
			if items < len(self.coefficients):
				return self.coefficients[items]
			else:
				return 0
		elif isinstance(items, slice):
			return (self[i] for i in range(items.start, items.stop, items.step if items.step is not None else 1))
		else:
			raise TypeError('__getitem__ items must be an int or a slice')
	
	def __init__(self, coefficients):
		#coefficients are a list of numbers with the i-th element being the coefficient a_i
		self.coefficients = coefficients
        

	def degree(self):
		#returning the index of the highest nonzero coefficient.
		return (len(self.coefficients)-1)

	def coefficients(self):
		#returns the list of coefficients
		return self.coefficients

	def __call__(self, x):
		#returns the value of the polynomial at index x
		return self.coefficients[x]

	def __add__(self, p):
		#returns the sum of two polynomials
		if isinstance(p, int):
			return Polynomial(self[0] + p, self.coefficients[1:])
		elif isinstance(p, Polynomial):
			coeffs = []
			for i in range(max(self.order, p.order) + 1):
				coeffs.append(self[i] + p[i])
			return Polynomial(coeffs)
		else: #if not int or polynomial
			raise ArithmeticError
		
	def __sub__(self, p):
    	#returns the difference of two polynomials
		if isinstance(p, int):
			return Polynomial(self[0] - p, *self.coefficients[1:])
		elif isinstance(p, Polynomial): #if polynomial
			coeffs = []
			for i in range(max(self.order, p.order) + 1):
				coeffs.append(self[i] - p[i])
			return Polynomial(coeffs)
		else: #if not int or polynomial
			raise ArithmeticError

	def __mul__(self, c):
		#returns the product of an integer and a polynomial, checks if c is int
		if isinstance(c, int):
			coeffs = []
			for coeff in self.coefficients:
				coeffs.append(c * coeff)
			return Polynomial(coeffs)
		else:
			raise ArithmeticError

	def __rmul__(self, c):
		#returns the product of an integer and a polynomial
		return self * c
        
	def __repr__(self):
		#returns string representation of polynomial
        
		output = ''
		first = True #første tallet
		for i in range(len(self.coefficients) - 1, -1, -1):
			if self.coefficients[i] != 0:
				#setter minus foran tallene om de er mindre enn 0
				if self.coefficients[i] < 0:
					output += '-' if first else ' - '
				elif not first:
					output += ' + '
				first = False
				if i == 0:
					output += '{}'.format(self.coefficients[i])
				else:
					output += '{}x{}'.format(self.coefficients[i], i)

		if len(output) == 0:
			return '0'

	def __eq__(self, p):
        #returns true if two polynomials have the same coefficients
		likt = 0
		for i in range(self.coefficients):
			if self[i] == p[i]:
				likt+=1
		if likt == len(self.coefficients):
			return True
		return False
        