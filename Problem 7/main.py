#!/usr/local/bin/python
from pprint import pprint as pp
import json
'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''
hundred  = map(lambda x: x + 1, range(100))
ten      = map(lambda x: x + 1, range(10))
thousand = map(lambda x: x + 1, range(1000))

def meredith(max):
	return get_all_primes(max)
def get_all_primes(max):
	res = []
	n = 1
	m = []
	while (len(res) <= max):
	# while n < max:
		m.append(n)
		if( isprime(n) ):
			res.append(n)
		n += 1
	return {'list': res, 'index': n}
def isprime(startnumber):
    startnumber*=1.0
    for divisor in range(2,int(startnumber**0.5)+1):
        if startnumber/divisor==int(startnumber/divisor):
            return False
    return True

result = meredith(10001)

result['len'] = len(result['list'])
# print result['index']
print json.dumps(result)