# -*- coding: utf-8 -*-

# William Duong, Nathan Whatley
# CPSC 335-01
# 14 March 2022

# Code for finding the Fibonacci sequence using two different algorithmic
# approaches (Exhaustive Pattern, Golden Ratio Approach)
import math


exSequence = [0]


def user_in():
	"""This function gets the input from the user for Part B"""
	while(True):

		p = input("Enter p, a positive integer:")
		p = int(n)
		if(f.is_integer(p)):
			break

		else:
			print("P must be a non floating point positive integer")
	while(True):

		n = input("Enter n, a positive integer:")
		n = int(n)
		if(f.is_integer(n)):
			break

		else:
			print("N must be a non floating point positive integer")

	goldenrat(n,p)


def goldenrat(n, p):
	"""This function calculates 3 different equations involving Golden Ratio"""
	#1 + 5^.5 / 2 == 1.61803
	
	fisq = math.sqrt(5)

	#Equation 3
	numerator = (1 + fisq) ** p - (1 - fisq) ** p
	denominator = (2**p) * (fisq)

	f_p = numerator / denominator
	f_p = int(f_p)
	# Equation 4
	final_n = f_p * ((1 + fisq) / 2)**(n-p)

	#Equation 5
	f_n_1 = f_p * ((1+ fisq) / 2)

	ratio_a = final_n/f_n_1

	fiba = list()
	for x in range(21):
		numerator = (1 + fisq) ** x - (1 - fisq) ** x
		denominator = (2**x) * (fisq)

		result_x = numerator / denominator
		result_x = int(result_x)

		fiba.append(result_x)
	
	result_string = "The result of n = {} and p = {} is:\n".format(n,p)
	result_string += "Equation 3  = {}, Equation 4 = {}, Equation 5 = {}\n".format(f_p, final_n, f_n_1)
	result_string += "The ratio between fn/fp should be approx to the Golden Ratio: {}\n".format(ratio_a)
	result_string += "The first 20 terms using EQ 3: \n"
	result_string += "{}".format(fiba)

	return result_string


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
	
	user_in()
