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

def TournamentSelection(P):
	"""
	Selects to Genomes from population at random and uniformly
	to use as parents.
	"""
	mt = MT()
	N = len(P)
	return P[mt.randint(0, N)]
	

def RankBiasedSelection(bias, P):
	"""
	Selects parent based on relative fitness.
	"""
	mt = MT()
	u = mt.uniform(0, 1)
	idx = math.floor( ((bias - math.sqrt(bias**2 - 4.0*(b - 1)*U)) / 2.0) / (b - 1)) 
	return P[idx]