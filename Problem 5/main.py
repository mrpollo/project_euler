#!/usr/local/bin/python
from pprint import pprint as pp
from decimal import Decimal
'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''
n = map(lambda x: x + 1, range(20))
t = map(lambda x: x + 1, range(10))

def meredith():
	r = 1
	while True:
		print '-- [ ' + str(r) + '] --'
		if(multiplies(r)):
			return r
		r += 1
def multiplies(v):
	res = []
	test = []
	for i in n:
		d = v / float(i)
		b = d.is_integer()
		# print str(v) + ' / ' + str(i) + ' = '
		# print d
		# print b
		if( b == False ):
			return False
		else:
			res.append(True)
	if( res.count(True) == 20 ):
		print '-------------------------------'
		print '-- [ ' + str(v) + '] --'
		print str(v) + ' / ' + str(i) + ' = '
		print d
		print str(v) + ': ' + str(res.count(True))
		pp(res)
		print '-------------------------------'
		return True
	return False

print meredith()