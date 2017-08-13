#/usr/bin/env python3
import sys

ans = []
for i in range(999, 99, -1):
    for j in range(999, i, -1):
        p = i*j
        if str(p) == "".join(reversed(str(p))):
            ans.append((p, i, j))

print(max(ans)[0])
