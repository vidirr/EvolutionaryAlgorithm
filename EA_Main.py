#! /usr/bin/env python2

from AlgorithmFactory import Algorithms


def f1_sol(N, iters=1000):

	algs = Algorithms
	return algs.BEA(N=N, xmin=-5.12, xmax=5.11, optimum=0)


def main():

	#TODO: Parse config.
	#I just don't feel like it right now.
	ans = f1_sol(N=1000)
	print ans

if __name__ == "__main__":
	main()