#! /usr/bin/env python2
from TestsFactory import Tests
from AlgorithmFactory import Algorithms
import sys


def f1_sol(N=1, popsize=1000, iters=1000):

	algs = Algorithms
	t = Tests
	return algs.BEA(N=N, popsize=popsize, xmin=-5.12, xmax=5.11, iters=500, test=t.f1)

def f2_sol(N=2, popsize=1000, iters=1000):

	algs = Algorithms
	t = Tests
	return algs.BEA(N=N, popsize=popsize, xmin=-2.048, xmax=2.047, iters=500, test=t.f2)

def f3_sol(N=2, popsize=1000, iters=1000):

	algs = Algorithms
	t = Tests
	return algs.BEA(N=N, popsize=popsize, xmin=-65.536, xmax=65.535, iters=500, test=t.shekel)


def f4_sol(N=10, popsize=1000, iters=1000):

	algs = Algorithms
	t = Tests
	return algs.BEA(N=N, popsize=popsize, xmin=-512.0, xmax=511, iters=500, test=t.rana)


def main():
	#Parsing command line arguments for now..
	#1 for f1, 2 for f2 etc.
	#This will of course be parsed from the config file like everything else.
	if(len(sys.argv) > 1):
		prob = sys.argv[1]
	else:
		prob = "1"

	#TODO: Parse config.
	#I just don't feel like it right now.
	if prob == "1":
		print "Solving De Jong F1 problem.."
		ans = f1_sol(N=1, popsize=100, iters=1000)
		print "Iteration {0}/{1}".format(1000, 1000)

	elif prob == "2":
		print "Solving De Jong F2 problem.."
		ans = f2_sol(N=2, popsize=100, iters=100)
		print "Iteration {0}/{1}".format(100, 100)

	elif prob == "3":
		print "Solving Shekel's Foxholes problem.."
		ans = f3_sol(N=2, popsize=100, iters=1000)
		print "Iteration {0}/{1}".format(1000, 1000)

	elif prob == "4":
		print "Solving Rana's function problem.."
		ans = f4_sol(N=10, popsize=500, iters=1000)
		print "Iteration {0}/{1}".format(1000, 1000)

	else:
		print "Invalid input."
		return
	print ans

if __name__ == "__main__":
	main()