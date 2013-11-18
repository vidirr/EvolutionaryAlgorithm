"""
Implementations of entities that are used to represent
entities in the problems of the De Jong's Test Suite.

"""
from Bitstring.bitstring import BitArray, BitStream
class GenomeF1:
	"""
		_value is the float representation of the binary string
		_dna is the binary representation of the entity
		_fitness is the fitness of the entity evaluated by the eval function.
	"""

	def __init__(self, value=None, DNA=None, fitness=None):

		#Used when creating the Genome with a random float number.
		if DNA is None:
			self._value = value
			self._dna = BitArray(float=value, length=32)
			self._fitness = None

		#Used when creating the Genome with a DNA string.
		elif value is None:
			self._dna = BitArray(DNA)
			self._value = self._dna.float
			self._fitness = None



	def __repr__(self):
		return "GenomeF1: " + "Fit: " + str(self._fitness) + "\n" + "DNA: " + str(self._dna.bin) + "\n\n"

	def setFitness(self, f):
		self._fitness = f

	def getFitness(self):
		return self._fitness

	def getDNA(self):
		return self._dna

	def getValue(self):
		return self._value




