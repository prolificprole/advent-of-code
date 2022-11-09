#!/usr/bin/python3

import sys

a=None
n=0

for line in sys.stdin:
	if not a:
		a = [0]*(len(line)-1)

	for i in range(len(line)-1):
		a[i] += int(line[i])

	n+=1

g = int(''.join(map (lambda c: '1' if c > n//2 else '0', a)), 2)
e = int(''.join(map (lambda c: '0' if c > n//2 else '1', a)), 2)
print(g*e)
