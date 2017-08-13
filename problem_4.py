#/usr/bin/env python3
import sys

for i in range(999, 99, -1):
    for j in range(999, 99, -1):
        p = str(i*j)
        if p == "".join(reversed(p)):
            print(p, i, j)
            sys.exit()
