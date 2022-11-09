#!/usr/bin/env python3

import sys

result = 0
last = None
for line in sys.stdin:
	n = int(line)
	if last != None and n > last:
		result += 1
	last = n

print(result)
