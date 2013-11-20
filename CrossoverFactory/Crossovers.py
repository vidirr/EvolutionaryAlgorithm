from EntitiesFactory.Entities import Genome
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
	c1col = []
	c2col = []
	
	for i in range( len(dna1) ):

		point = mt.randint(0, len(dna1[i].bin) - 1)
		#Crossover
		x, y = dna1[i].bin, dna2[i].bin
		c1 = x[:point] + y[point:]
		c2 = y[:point] + x[point:]

		c1col.append(c1), c2col.append(c2)
	return Genome(DNA=c1col), Genome(DNA=c2col)


def TwoPointCrossover(g1, g2, mt):


	def sort(p1, p2):
		return (p1, p2) if (p1 < p2) else (p2, p1)

	dna1, dna2 = g1.getDNA(), g2.getDNA()
	c1col = []
	c2col = []

	for i in range( len(dna1) ):

		p1 =  mt.randint(0, len(dna1[i].bin) - 1)
		p2 =  mt.randint(0, len(dna1[i].bin) - 1)

		p1 , p2 = sort(p1, p2)

		x, y = dna1[i].bin, dna2[i].bin

		c1 = x[:p1] + y[p1:p2] + x[p2:]
		c2 = y[:p1] + x[p1:p2] + y[p2:]

		c1col.append(c1)
		c2col.append(c2)

	return Genome(DNA=c1col), Genome(DNA=c2col)

def UniformCrossover(g1, g2, mt):
	"""
	DOES NOT WORK, BUT WOULD IMPROVE PERFORMANCE.

	import copy

	c1 = copy.deepcopy(g1)
	c2 = copy.deepcopy(g2)

	for i in range( len(c1.getDNA()) ):

		#Select random number of bits to crossover.
		for _ in range(mt.randint(1, len(c1.getDNA()[i].bin))):

			bit = mt.randint(0, len(c1.getDNA()[i].bin) - 1)
			temp = c1.getDNA()[i][bit]
			c1.getDNA()[i].set(c2.getDNA()[i][bit], bit)
			c2.getDNA()[i].set(temp, bit)


	return c1, c2

	"""


	dna1, dna2 = g1.getDNA(), g2.getDNA()
	c1col = []
	c2col = []

	for i in range( len(dna1) ):

		c1 = list(dna1[i].bin)
		c2 = list(dna2[i].bin)

		#Select random number of bits to crossover.
		for _ in range(mt.randint(1, len(dna1[i].bin))):

			bit = mt.randint(0, len(dna1[i].bin) - 1)
			c1[bit], c2[bit] = c2[bit], c1[bit]
			
		map(str, c1)
		map(str, c2)

		c1s = ""
		c2s = ""

		for i in range(len(c1)):
			c1s += c1[i]
			c2s += c2[i]

		c1col.append(c1s)
		c2col.append(c2s)

	return Genome(DNA=c1col), Genome(DNA=c2col)
