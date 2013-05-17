def primes(n):
    s=range(0,n+1)
    s[1]=0
    bottom=2
    top=n//bottom
    while (bottom*bottom<=n):
        while (bottom<=top):
            if s[top]:
                s[top*bottom]=0
            top-=1
        bottom+=1
        top=n//bottom
    return [x for x in s if x]

vals = primes(2000000)
sums = 0
for x in vals:
    sums += x
print sums
