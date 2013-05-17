#!/usr/local/bin/python
from pprint import pprint as pp
import json
'''
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025  385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''
hundred  = map(lambda x: x + 1, range(100))
ten      = map(lambda x: x + 1, range(10))
thousand = map(lambda x: x + 1, range(1000))

def meredith(set):
	return {'sum': sum_of_squares(set), 'square': square_of_sum(set)}
def sum_of_squares(set):
	res = 0
	for i in set:
		res += i*i
	return res
def square_of_sum(set):
	res = 0
	for i in set:
		res += i
	return res*res

# pp(hundred)
set_results = meredith(hundred)
set_results['result'] = set_results['square'] - set_results['sum']
print json.dumps(set_results)