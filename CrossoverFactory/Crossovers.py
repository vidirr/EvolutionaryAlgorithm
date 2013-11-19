from EntitiesFactory.Entities import GenomeF1
#USED INSTEAD OF RANDOM
from MTrandom.MTrandom import  MersenneTwister as MT
from Bitstring.bitstring import BitArray, BitStream



def OnePointCrossover(g1, g2, mt):
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


	#We get two double arrays, dna1 == [[1010110...], [011101101..], ] etc.
	dna1, dna2 = g1.getDNA(), g2.getDNA()
	c1col = [], c2col = []
	
	for i in range( len(dna1) ):

		point = mt.randint(0, len(dna1))
		#Crossover
		x, y = dna1[i], dna2[i]
		c1 = x[:point] + y[point:]
		c2 = y[:point] + x[point:]

		c1col.append(c1), c2col.append(c2)
	#import pdb; pdb.set_trace()

	return GenomeF1(DNA=c1col), GenomeF1(DNA=c2col)