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
	pop = sorted(pop, lambda x: x.getFitness())
	cpop = sorted(cpop, lambda x: x.getFitness())
	newpop = []
	# 10% of best parents might survive.
	idx = len(pop) / 10

	#Make sure we only replace with better children.
	for i in range(idx):
		newpop.append(pop[idx]) if (pop[idx].getFitness() < cpop[idx].getFitness()) else newpop.append(cpop[idx])
	newpop += cpop[idx:]

	return random.shuffle(newpop)


def ElitismSelection(pop, cpop):
	"""
	Take some small number of the best parents
	and keep them in place of the worst offspring
	(if they're better). Strengthens convergence,
	but may result in premature convergence.

	"""
	pass

def TruncationSelection(pop, cpop):
	"""
	 Take the best N from the union of parent and
	offspring populations. Very strong selection, 
	needs to be balanced with something else to avoid 
	premature convergence problems.

	"""
	pass