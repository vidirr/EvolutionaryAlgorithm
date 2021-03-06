
#USED INSTEAD OF RANDOM
from MTrandom.MTrandom import  MersenneTwister as MT
from TestsFactory import Tests as T
from SelectionMethodFactory import SelectionMethods as SM
from CrossoverFactory import Crossovers as CO
from ReplacementMethodFactory import ReplacementMethods as RM
from EntitiesFactory.Entities import Genome

#Just used for shuffle-ing
import random
import math


#Arrays that map string names to functions
test_functions = {
    'F1' : T.f1,
    'F2' : T.f2,
    'Rana' : T.rana,
    'Shekel' : T.shekel,
}

selection_schemes = {
    "Roulette" : SM.RouletteWheelSelection,
    "Tournament" : SM.TournamentSelection,
    "RankBiased" : SM.RankBiasedSelection,
    "Random"	 : SM.RandomSelection,
}

crossover_types = {
    "OnePoint" : CO.OnePointCrossover,
    "TwoPoint" : CO.TwoPointCrossover,
    "Uniform"  : CO.UniformCrossover,
    "Random"   : CO.RandomCrossover,
}

replacement_methods = {
    "Generational" : RM.GenerationalReplacement,
    "Elitism" : RM.ElitismReplacement,
    "Truncation" : RM.TruncationReplacement,
    "SteadyState" : RM.SteadyStateReplacement,
    "Random"	  : RM.RandomReplacement,
}

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


def mutate(c, chance, mt):

	#if mt.genrand_real1() <= chance:

	chrom = c.getDNA()[mt.randint( 0, len(c.getDNA()) - 1)]
	bit = mt.randint(0, len(chrom.bin) - 1)
	chrom.invert(bit)

def BEA(N, popsize, xmin, xmax, testfunc, iters, crossover, selection, mutation, replacement):
	"""  
		Implementation of the BasicEvolutionaryAlgorithm as presented
		in the slides.

	"""
	import time; t1 = time.time()
	test = test_functions[testfunc]
	mt = MT()
	cnt, Done = 0, False

	fitnesscalls = 0

	P = [Genome(N=N, mt=mt, xval=(xmin, xmax)) for _ in xrange(popsize)]
	import random; random.shuffle(P)
	#Evaluate the fitness level of all Genomes.
	print "Evaluating fitness level of initial population..",
	for g in P:
		g.setFitness( test(g.getValues()) )
		fitnesscalls += 1

	print "Done.\nStarting algorithm.\n"
	while cnt < iters and not Done:
		fprint("Iteration {0}/{1}\r".format(cnt, iters))
		cnt += 1
		cpop = []
		better = False
		
		while len(cpop) < popsize and not Done:
			#Select random parents
			p1, p2 = selection_schemes[selection](P, mt), selection_schemes[selection](P, mt)
			c1, c2 = crossover_types[crossover](p1, p2, mt)

			#Set the fitness of the new children by sending a list of 1
			#individual into the test function.
			c1.setFitness( test(c1.getValues() ))
			fitnesscalls += 1
			c1.setNrOfFitnessCalls(fitnesscalls)
			c2.setFitness( test(c2.getValues() ))
			fitnesscalls += 1
			c2.setNrOfFitnessCalls(fitnesscalls)
			mutate(c1, mutation, mt)
			mutate(c2, mutation, mt)

			#This shouldn't be here under normal circumstances - but seeing that python can represent pretty huge floating point numbers
			#we're sometimes able to find a better solution outside of the range of the problem.
			#So - to make sure that we solve the problem within the range of the problem we use this.
			if inrange(c1.getValues(), (xmin, xmax)): 
				cpop.append(c1)
			if inrange(c2.getValues(), (xmin, xmax)):
				cpop.append(c2)

		P = replacement_methods[replacement](P, cpop)
		if (time.time() - t1) > 120:
			Done = True

	#print P
	return sorted(P, key=lambda x: x.getFitness())[0]