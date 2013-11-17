#Genome entity - used to represent individuals in population.


class Genome:

	def __init__(self):

		self._fitness = None
		self._pos = None

	def setFitness(self, f):
		self._fitness = f

	def getFitness(self, f):
		return self._fitness

