from EntitiesFactory.Entities import GenomeF1
from TestsFactory import Tests as T
from EvaluationMethodFactory import EvaluationMethods as EM
#USED INSTEAD OF RANDOM
from MTrandom.MTrandom import  MersenneTwister as MT


def BEA(N, xmin, xmax, optimum, iters=1000):
	"""  
		Implementation of the BasicEvolutionaryAlgorithm as presented
		in the slides.

	"""

	mt = MT()
	cnt, Done = 0, False

	#Initial population
	P = [GenomeF1(mt.uniform(xmin, xmax)) for _ in xrange(N)]
	print P
	while cnt < iters and not Done:

		cpop = []
		#while len(cpop) < N:


		ans = T.f1(P)
		print ans
		return
		#Select parent pool from P


	return "foobang"