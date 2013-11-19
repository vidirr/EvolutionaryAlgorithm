"""
	

"""
import random

def Generational(pop, cpop):
	"""
	Simply replaces the entire population with the new population.

	"""
	return cpop

def SteadyStateSelection(pop, cpop):
	"""
	Fewer parents then offspring.
	Some parents always survive.

	"""



def ElitismSelection(pop, cpop):
	"""
	Take some small number of the best parents
	and keep them in place of the worst offspring
	(if they're better). Strengthens convergence,
	but may result in premature convergence.

	"""
	pop = sorted(pop, key=lambda x: x.getFitness())
	cpop = sorted(cpop, key=lambda x: x.getFitness())[::-1]
	newpop = []
	# 10% of best parents might survive.
	idx = len(pop) / 10

	#Make sure we only replace with better children.
	newpop = pop[:idx] + cpop[idx:]

	#print "Length: " + str(len(newpop)) + "\n"
	#mport time; time.sleep(1)
	return newpop


def TruncationSelection(pop, cpop):
	"""
	 Take the best N from the union of parent and
	offspring populations. Very strong selection, 
	needs to be balanced with something else to avoid 
	premature convergence problems.

	"""
	pass