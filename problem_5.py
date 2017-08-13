#/usr/bin/env python3
from collections import Counter
from problem_3 import factorize
from functools import reduce

def add(prev, next_):
    for k, v in next_.items():
        prev[k] = max(prev[k], next_[k])
    return prev

counters = [Counter(factorize(i)) for i in range(2, 21)]
counters = reduce(add, counters, Counter())

ans = 1
for key, value in counters.items():
    ans *= key**value

print(ans)
