#!/usr/bin/env python

""" 
 A Rerverse Polish Notation calculator in python
 > 19 2.14 + 4.5 2 4.3 / - *
 only supports two operands and then an operator 
"""

import sys, math, operator

"Valid operators"
operators = {'+':operator.add,
       '-':operator.sub,
       '*':operator.mul,
       '/':operator.div,
       'v':operator.pow,
       'sin':math.sin,
       'cos':math.cos,
}

"functiom that evaluates the expression given in the command line"
def exp(args, stack):
    for arg in args:
        if set(arg).issubset(set('0123456789')):
            stack.append(float(arg))
        elif arg in operators:
            if len(stack) < 2:
                 raise ValueError('Must have at least two parameters to perform operation')
            a = stack.pop()
            b = stack.pop()
            op = operators[arg]
            stack.append(op(b,a))
        elif arg == 'p':
            print [stack[-1]]
    return stack
 
if __name__ == '__main__':     
	stack = []
	while True:
		expression = sys.raw_input('> ')
		if expression in ['quit', 'q', 'exit']:
			exit()
		elif expression in ['clear', 'c', 'empty']:
			stack = []
			continue
		stack = exp(exp.split(), stack)
		print [stack]
		
		