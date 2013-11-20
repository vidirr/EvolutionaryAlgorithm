"""
	Implementations of different selection methods.

"""
from MTrandom.MTrandom import  MersenneTwister as MT
import math

def RouletteWheelSelection():
	"""
	We need to change the Genome class if we want to use this method,
	since each instance gets a probability in proportion to the amount
	of the total amount of total population fitness contributed by that
	instance.

	P(C) = fitness(C) / [sum += c.getFitness() for c in P]
	"""
	pass

def TournamentSelection(P, mt):
	"""
	Selects to Genomes from population at random and uniformly
	to use as parents.
	"""
	N = len(P)
	return P[mt.randint(0, N - 1)]
	

def RankBiasedSelection(P, mt):
	"""
	Selects parent based on relative fitness.
	"""
	pop = sorted(P, key=lambda x: x.getFitness())
	#b = 3.5
	b = 3
	U = mt.uniform(0, 1)
	idx =  len(P)*( (b - math.sqrt(b**2 - 4.0*(b - 1)*U)) / 2.0)
	idx = idx / (b - 1)
	idx = math.floor(idx)
	idx = int(idx)
	return pop[idx] 

def RandomSelection(P, mt):

	sel = mt.randint(0, 1)

	if sel == 0:
		return TournamentSelection(P, mt)
	else:
		return RankBiasedSelection(P, mt)