"""
Implementations of entities that are used to represent
entities in the problems of the De Jong's Test Suite.

"""
from Bitstring.bitstring import BitArray, BitStream
class GenomeF1:

	def __init__(self, fitness):

		self._fitness = fitness
		self.setDNA()

	def __repr__(self):
		return "GenomeF1: " + "Fit: " + str(self._fitness) + "\n" + "DNA: " + str(self._dna.bin) + "\n\n"

	def getFitness(self):
		return self._fitness

	def setDNA(self):
		self._dna = BitArray(float=self._fitness, length=32)

	def getDNA(self):
		return self._dna




