 
from EvaluationMethodFactory import EvaluationMethods as EM
#USED INSTEAD OF RANDOM
from MTrandom.MTrandom import  MersenneTwister as MT
from SelectionMethodFactory import SelectionMethods as SM
from CrossoverFactory import Crossovers as CO
from ReplacementMethodFactory import ReplacementMethods as RM
from EntitiesFactory.Entities import Genome

#Just used for shuffle-ing
import random
import math

def fprint(n):
	import sys
	sys.stdout.write(n)
	sys.stdout.flush()

def inrange(vals, range):
	for v in vals:
		if range[0] <= v <= range[1]:
			continue
		else:
			return False
	return True


def BEA(N, popsize, xmin, xmax, test, iters):
	"""  
		Implementation of the BasicEvolutionaryAlgorithm as presented
		in the slides.

	"""
	mt = MT()
	cnt, Done = 0, False

	print "Configuration:\n============\nN: {0}\nPopulation size: {1}\nRange: {2}\nIterations: {3}\n".format(N, popsize, (xmin, xmax), iters)
	#Initial population
	print "initializing population.."
	P = [Genome(N=N, mt=mt, xval=(xmin, xmax)) for _ in xrange(popsize)]
	import random; random.shuffle(P)
	#Evaluate the fitness level of all Genomes.
	print "Evaluating fitness level of initial population..",
	for g in P:
		g.setFitness( test(g.getValues()) )

	print "Done.\nStarting algorithm.\n"
	while cnt < iters and not Done:
		fprint("Iteration {0}/{1}\r".format(cnt, iters))
		cnt += 1
		cpop = []
		
		while len(cpop) < popsize:
			#Select random parents
			#TODO: Make SelectionMethod and CrossoverMethod parameters
			#to the algorithm so that it can be envoked for any problem.
			p1, p2 = SM.TournamentSelection(P, mt), SM.TournamentSelection(P, mt) 
			c1, c2 = CO.TwoPointCrossover(p1, p2, mt)

			#TODO: Implement mutation.
			#mutate(c1, c2)

			#Set the fitness of the new children by sending a list of 1
			#individual into the test function.
			c1.setFitness( test(c1.getValues() ))
			c2.setFitness( test(c2.getValues() ))

			if inrange(c1.getValues(), (xmin, xmax)) and inrange(c2.getValues(), (xmin, xmax)):
				cpop.append(c1) if (math.fabs(c1.getFitness()) < math.fabs(c2.getFitness())) else cpop.append(c2)
			elif inrange(c1.getValues(), (xmin, xmax)) and not inrange(c2.getValues(), (xmin, xmax)):
				cpop.append(c1)
			elif inrange(c2.getValues(), (xmin, xmax)):
				cpop.append(c2)

		P = RM.ElitismSelection(P, cpop)

	#print P
	return sorted(P, key=lambda x: x.getFitness())[0]