# -*- coding: utf-8 -*-

# William Duong, Nathan Whatley
# CPSC 335-01
# 07 March 2022

# Code for finding the Fibonacci sequence using two different algorithmic
# approaches (Exhaustive Pattern, Golden Ratio Approach)

exSequence = [0]


def exhaustive(n):
	"""Fibonacci sequence using Exhaustive Pattern"""
	global exSequence

	if len(exSequence) == 1:
		exSequence.append(1)
	else:
		exSequence.append(sum(exSequence[n-1:n+2]))

	while len(exSequence) != 16:
		exhaustive(n+1)



if __name__ == "__main__":
	"""Main function"""

	# Using the recursive exhaustive pattern method
	exhaustive(0)
	print("Part 1A (Recursive Exhaustive Pattern): {}\n".format(exSequence[-1]))