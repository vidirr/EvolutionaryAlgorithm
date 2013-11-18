from EntitiesFactory.Entities import GenomeF1
from TestsFactory import Tests as T
from EvaluationMethodFactory import EvaluationMethods as EM
#USED INSTEAD OF RANDOM
from MTrandom.MTrandom import  MersenneTwister as MT
from SelectionMethodFactory import SelectionMethods as SM
from CrossoverFactory import Crossovers as CO


def BEA(N, xmin, xmax, optimum, iters=1000):
	"""  
		Implementation of the BasicEvolutionaryAlgorithm as presented
		in the slides.

	"""

	mt = MT()
	cnt, Done = 0, False

	#Initial population
	P = [GenomeF1(value=mt.uniform(xmin, xmax)) for _ in xrange(N)]
	#Evaluate the fitness level of all genomes.
	for g in P:
		g.setFitness( T.f1(g.getValue()) )
	print P
	while cnt < iters and not Done:

		cpop = []
		while len(cpop) < N:
			#Select random parents
			p1, p2 = SM.TournamentSelection(P), SM.TournamentSelection(P) 
			c1, c2 = CO.OnePointCrossover(p1, p2)
			mutate(c1, c2)
			evaluate(c1, c2)
			cpop.append(c1)
			cpop.append(c2)

		P = cpop
		print ans
		return
		#Select parent pool from P


	return "foobang"