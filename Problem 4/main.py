#!/usr/local/bin/python
import pprint
'''
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 99.
Find the largest palindrome made from the product of two 3-digit numbers.
012345
0=5
1=4
2=3
'''
def palCheck(x):
	n = str(x)
	if( n[0] == n[5] and n[1] == n[4] and n[2] == n[3] ):
		return True
	return False
def loopPal():
	a_mult = 999
	b_mult = 999
	output = []
	for a in range(a_mult, -1, -1):
		if ( a > 99 ):
			for b in range(b_mult, -1, -1):
				if( b > 99 ):
					c = a * b
					if( len(str(c)) > 5 ):
						if( palCheck(c) ):
							output.append(c)
	return output
pprint.pprint( sorted(loop()) )