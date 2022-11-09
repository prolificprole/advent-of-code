#!/usr/bin/python3

import sys

def num_set_bits(cands, pos):
	n = 0
	for cand in cands:
		if cand[pos] == '1':
			n+=1
	return n

def filter(cands, calculate_match_bit):
	n = 0
	while len(cands) != 1:
		v = calculate_match_bit(cands, n)
		newcands = []

		for cand in cands:
			if cand[n] == v:
				newcands.append(cand)
		cands = newcands
		n+=1

	return cands[0]

cands = []
for line in sys.stdin:
	cands.append(line.strip())

oxygen = int(filter(cands, lambda cands, n: '1' if 2*num_set_bits(cands, n) >= len(cands) else '0'), 2)
co2 = int(filter(cands, lambda cands, n: '0' if 2*num_set_bits(cands, n) >= len(cands) else '1'), 2)

print(oxygen*co2)
