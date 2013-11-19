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

	def __init__(self, mt=None, xval=None, value=None, DNA=None, fitness=None):

		#Used when creating the Genome with a random float number.
		if mt is not None:
			if xval is None:
				#Should raise a custom exception.
				raise Exception
			#xval is the touple (xmin, xmax)
			xmin, xmax = xval
			self._value = mt.uniform(xmin, xmax)
			self._dna = BitArray(float=self._value, length=32)
			return

		elif DNA is None:
			self._value = value
			self._dna = BitArray(float=value, length=32)
			self._fitness = None
			return

		#Used when creating the Genome with a DNA string.
		elif value is None:
			#Make sure we get the 0b at the beginning of the string.
			#This is used to represent binary strings in Python.
			DNA = DNA if (DNA[2:] != '0b') else '0b' + DNA
			self._dna = BitArray(DNA)
			self._value = self._dna.float
			self._fitness = None
			return


	def __repr__(self):
		return "Genome type: F1\n" + "Fit: " + str(self._fitness) + "\n" + "DNA: " + str(self._dna.bin) + "\n\n"

	def setFitness(self, f):
		self._fitness = f

	def getFitness(self):
		return self._fitness

	def getDNA(self):
		return self._dna

	def getValue(self):
		return self._value

class GenomeF2:
	"""
		F2 has a different representation of the problem since it uses a
		vector of 2 to represent itself. 

	"""
	pass


