# -*- coding: utf-8 -*-

# William Duong, Nathan Whatley
# CPSC 335-01
# 14 February 2022

# Code for ...
import math

def user_in():
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


def goldenrat(n, p):
	#1 + 5^.5 / 2 == 1.61803
	#f of p == 
	fisq = math.sqrt(5)

	numerator = (1 + fisq) ** p - (1 - fisq) ** p
	#print(numerator)
	denominator = (2**p) * (fisq)

	result = numerator / denominator
	#print(result)
	final_n = result * ((1 + fisq) / 2)**(n-p)

	return final_n

print(goldenrat(2, 1))