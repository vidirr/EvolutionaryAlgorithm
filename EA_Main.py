#! /usr/bin/env python2
import random
from Tests import TestFactory
from MTrandom.MTrandom import  MersenneTwister as MT





def f1_sol(N, iters=1000):

	#Get access to test function module.
	t = TestFactory

	#MresenneTwister random generator - Python port of the code
	#that is given for mtrandom on MySchool.
	mt = MT()

	#Given in defenition of problem 1
	xmin = -5.12
	xmax = 5.11




	i = 0
	Done = False
	#Just a random number, basically just can't be 0
	#and has to be high since we're approaching 0
	sol = 10**10

	#Initial population
	P = [mt.uniform(xmin, xmax) for _ in range(N)]
	while i < iters and not Done:
		ans = t.f1(P)
		print ans
		return
		#Select parent pool from P






def main():

	f1_sol(1000)


if __name__ == "__main__":
	main()