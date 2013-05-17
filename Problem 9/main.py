'''
A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

'''

def main():
    for a in range(1, 501):
        for b in range(a, 501):
            if ((a*a) + (b*b) == (1000-a-b) * (1000-a-b)):
                return a * b * (1000-a-b)
    return "chow"

print main()
