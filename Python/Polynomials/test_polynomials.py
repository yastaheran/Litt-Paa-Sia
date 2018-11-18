#!/usr/bin/env python

from polynomials import * 

p = Polynomials([1,7,3])
q = Polynomials([2,4])
r = Polynomials([1,7,3])

# A test verifying that evaluating a polynomial of your choice at 3 different points gives what you’d expect
def test_evalPolynomial():
	assert p.__eq__(r) == True

# A test verifying that adding two polynomials of your choice returns what it’s supposed to
def test_adding():
	assert p.__add__(q) == [3,11,3]

# A test verifying that subtracting two polynomials of your choice returns what it’s supposed to
def test_subtracting(self, poly2):
	assert p.__sub__(q) == [-1,3,3]
	
# A test verifying that each polynomial has a .degree() method which returns its degree
def test_degree():
	assert p.degree() == 2
	
# A test verifying that multiplying two polynomials of your choice returns what it’s supposed to
def test_multi():
	
	
# A test verifying that multiplying an polynomial and an int of your choice returns what it’s supposed to
def test_rmulti():
	
	
# A test verifying that multiplying two polynomials of your choice returns what it’s supposed to
def test_repr():
	