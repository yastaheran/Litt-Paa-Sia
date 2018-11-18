#!/usr/bin/env python
class UnitTest(object):
	
		
    def __init__(self, func, args, kwargs, res):    # the constructor
		self.func = func
		self.args = args
		self.kwargs = kwargs
		self.res = res
		
    def __call__(self):                             # run test
		
		result = self.func(self.args, self.kwargs)
		
		if result = self.res:
			return True
		elif result != self.res:
			return False
		else:
			raise ValueError("something went wrong")