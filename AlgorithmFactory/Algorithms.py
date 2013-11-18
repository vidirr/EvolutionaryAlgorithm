
from EvaluationMethodFactory import EvaluationMethods as EM
#USED INSTEAD OF RANDOM
from MTrandom.MTrandom import  MersenneTwister as MT
from SelectionMethodFactory import SelectionMethods as SM
from CrossoverFactory import Crossovers as CO

#Just used for shuffle-ing
import random

def fprint(n):
	import sys
	sys.stdout.write(n)
	sys.stdout.flush()

def BEA(N, xmin, xmax, genome, test, iters=1000):
	"""  
		Implementation of the BasicEvolutionaryAlgorithm as presented
		in the slides.

	"""
	mt = MT()
	cnt, Done = 0, False

	#Initial population
	P = [genome(value=mt.uniform(xmin, xmax)) for _ in range(N)]

	#Evaluate the fitness level of all genomes.
	for g in P:
		g.setFitness( test([g.getValue()]) )
	while cnt < iters and not Done:
		fprint("Iteration " + str(cnt) + "/" + str(iters) + "\r")
		cnt += 1
		random.shuffle(P)
		cpop = []
		while len(cpop) < N:
			#Select random parents
			p1, p2 = SM.TournamentSelection(P, mt), SM.TournamentSelection(P, mt) 
			c1, c2 = CO.OnePointCrossover(p1, p2, mt)
			#mutate(c1, c2)
			#Set the fitness of the new children by sending a list of 1
			#into the test function.
			c1.setFitness( test([c1.getValue()]))
			c2.setFitness( test([c2.getValue()]))
			cpop.append(c1) if c1.getFitness() < c2.getFitness() else cpop.append(c2)

		P = cpop
		P = sorted(P)
		#print "Best:", P[0], "Worst:", P[-1]
		#Select parent pool from P


	return P[0]