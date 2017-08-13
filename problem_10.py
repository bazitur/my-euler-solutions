#/usr/bin/env python3

from collections import OrderedDict

def primes_below(n):
    arr = OrderedDict((i, True) for i in range(2, n+1))
    for k, v in arr.items():
        if v:
            for x in range(k*2, n+1, k):
                arr[x] = False
    return [k for k, v in arr.items() if v]

print(sum(primes_below(int(input("Print primes below: ")))))
