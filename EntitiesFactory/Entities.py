"""
Implementations of entities that are used to represent
entities in the problems of the De Jong's Test Suite.

"""
from Bitstring.bitstring import BitArray, BitStream
class Genome:
	"""
		_values is a list of the float values that define the current entity.
		_dna is a list of the binary representations of the entity values
		_fitness is the fitness of the entity evaluated by the eval function.

		N defines the number of values the current individual stores.
	"""

	def __init__(self, N=None, mt=None, xval=None, value=None, DNA=None, fitness=None):

		self._values = []
		self._dna = []
		self._fitness = None #Uninitialzed
		#Used in Roulette Wheel Selection
		self._P = None
		#Used for statistics
		self._fitnessCalls = None

		if mt:
			xmin, xmax = xval
			for _ in range(N):
				cval = mt.uniform(xmin, xmax)
				self._values.append(cval)
				self._dna.append(BitArray(float=cval, length=32))
		#If we get a list of DNA strings (from crossover for example) we just append the values of the DNA string into values.
		elif DNA:
			for d in DNA:
				#Make sure we get the 0b at the front of the string.
				d = d if(d[2:] != '0b') else '0b' + d
				d = BitArray(bin=d)
				#Store strings
				self._dna.append(d)
				#And values of the strings
				self._values.append(d.float)
		
	def __repr__(self):

		rep = "Fitness level: {0} - Fitness callls: {1}\n".format(self._fitness, self._fitnessCalls)
		for i in range(len(self._values)):
		 	rep += 'Chromosome {0} - Val: {1} - DNA: {2} \n'.format(i, self._values[i], self._dna[i].bin)
		return rep


	def setFitness(self, f):
		self._fitness = f

	def getFitness(self):
		return self._fitness

	def getDNA(self):
		return self._dna

	def getValues(self):
		return self._values

	#Used for statistics
	def setNrOfFitnessCalls(self, n):
		self._fitnessCalls = n

	def getNrOfFitnessCalls(self):
		return self._fitnessCalls


