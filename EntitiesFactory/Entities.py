"""
Implementations of entities that are used to represent
entities in the problems of the De Jong's Test Suite.

"""

import struct
def binary(num):
    return ''.join(bin(ord(c)).replace('0b', '').rjust(8, '0') for c in struct.pack('!f', num))



class GenomeF1:

	def __init__(self, fitness):

		self._fitness = fitness
		self.setDNA()

	def __repr__(self):
		return "GenomeF1: " + str(self._fitness) + " - " + str(self._dna) 

	def getFitness(self):

		return self._fitness

	def setDNA(self):
		self._dna = binary(self._fitness)

	def getDNA(self):
		return self._dna



