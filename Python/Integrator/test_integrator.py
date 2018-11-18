#!/usr/bin/env python

from integrator import * 

""" verify that if you use the integrate function to integrate f(x) = 2 from 0 to 1 
numerically, you get (up to roundoff errors) 2 no matter what N is """
def test_integral_of_constant_function(N):
	expected_answer = 2
	computed_answer = integrator(function, 0, 1, N)
	assert(expected_answer - computed_answer) == 2
	
	
""" verify that if you integrate f(x) = 2x from 0 to 1 numerically,
you get about 1, with the error being about 1/N. """
def test_integral_of_linear_function(N):
	expected_answer = 1/N
	computed_answer = integrator(function, 0, 1, N)
	abs(computed_answer - expected_answer) <  1E-15

""" verify that if you use the integrate function to integrate f(x) = 2 from 0 to 1 
numerically, you get (up to roundoff errors) 2 no matter what N is """
def test_numpy_integral_of_constant_function(N):
	expected_answer = 2
	computed_answer = numpy_integrator(function, 0, 1, N)
	assert(expected_answer - computed_answer) == 2
	
	
""" verify that if you integrate f(x) = 2x from 0 to 1 numerically,
you get about 1, with the error being about 1/N. """
def test_numpy_integral_of_linear_function(N):
	expected_answer = 1/N
	computed_answer = numpy_integrator(function, 0, 1, N)
	abs(computed_answer - expected_answer) <  1E-15