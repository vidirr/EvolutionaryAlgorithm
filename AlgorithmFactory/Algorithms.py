from TestsFactory import Tests

#USED INSTEAD OF RANDOM
from MTrandom.MTrandom import  MersenneTwister as MT
mt = MT()

def BEA(N, xmin, xmax, optimum, iters=1000):
	"""  
		Implementation of the BasicEvolutionaryAlgorithm as presented
		in the slides.

	"""

	cnt, Done = 0, False

	#Initial population
	P = [mt.uniform(xmin, xmax) for _ in range(N)]
	
	while cnt < iters and not Done:
		ans = Tests.f1(P)
		print ans
		return
		#Select parent pool from P


	return "foobang"