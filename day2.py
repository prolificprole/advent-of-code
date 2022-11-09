#!/usr/bin/env python3

import sys

z = 0
y = 0
for line in sys.stdin:
	(direction, val) = line.split()
	if direction == 'forward':
		y += int(val)
	elif direction == 'up':
		z -= int(val)
	elif direction == 'down':
		z += int(val)

print(z*y)
