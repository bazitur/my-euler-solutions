#/usr/bin/env python3
from functools import reduce
from operator import add

n = int(input("Constant: "))
s1 = reduce(add, (i**2 for i in range(1, n+1)), 0)
print((n*(n+1)/2)**2 - s1)
