#!/usr/bin/env python3

import sys

z = 0
y = 0
aim = 0
for line in sys.stdin:
	(direction, val) = line.split()
	if direction == 'forward':
		y += int(val)
		z += aim*int(val)
	elif direction == 'up':
		aim -= int(val)
	elif direction == 'down':
		aim += int(val)

print(z*y)
