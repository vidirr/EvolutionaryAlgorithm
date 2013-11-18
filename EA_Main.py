#! /usr/bin/env python2
from TestsFactory import Tests
from AlgorithmFactory import Algorithms
from EntitiesFactory.Entities import GenomeF1
import sys


def f1_sol(N, iters=1000):

	algs = Algorithms
	t = Tests
	return algs.BEA(N=N, xmin=-5.12, xmax=5.11, genome=GenomeF1, test=t.f1)

def f2_sol(N, iters=1000):

	algs = Algorithms
	t = Tests
	return algs.BEA(N=N, xmin=-2.048, xmax=2.047, genome=GenomeF1, test=t.f2)


def main():
	if(len(sys.argv) > 1):
		prob = sys.argv[1]

	#TODO: Parse config.
	#I just don't feel like it right now.
	if prob == "1":
		ans = f1_sol(1000)
	elif prob == "2":
		ans = f2_sol(1000)
	else:
		print "Invalid input."
		return
	print ans

if __name__ == "__main__":
	main()