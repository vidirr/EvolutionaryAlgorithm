from EntitiesFactory.Entities import GenomeF1
#USED INSTEAD OF RANDOM
from MTrandom.MTrandom import  MersenneTwister as MT


def OnePointCrossover(g1, g2):
	"""
	We select a single point, and splice the DNA of both parents
	together at that point to construct 2 new childs that share some
	DNA from both parents.

	Examples:
	======================================
	From 0 to 4:
	a = "123456789" --> a[:4] == "1234"
	From 4 to 9:
	a = "123456789" --> a[4:] == "56789"
	======================================
	"""

	mt = MT()
	point = mt.random(0, len(g1.bin))

	#Crossover
	dna1, dna2 = g1.getDNA(), g2.getDNA()

	c1 = dna1[:point] + dna2[point:]
	c2 = dna2[:point] + dna1[point:]

	return GenomeF1(DNA=c1), GenomeF1(DNA=c2)