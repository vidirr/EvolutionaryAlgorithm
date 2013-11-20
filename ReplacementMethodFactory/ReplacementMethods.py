"""
	

"""
import random

def GenerationalReplacement(pop, cpop):
	"""
	Simply replaces the entire population with the new population.

	"""
	random.shuffle(cpop)
	return cpop

def SteadyStateReplacement(pop, cpop):
	"""
	Fewer parents then offspring.
	Some parents always survive.

	"""
	idx = (len(pop)/10)
	random.shuffle(pop)
	random.shuffle(cpop)
	cpop = pop[:idx] + cpop[idx:len(pop)]
	return cpop
	#return sorted(pop, key=lambda x: x.getFitness())[:idx] + sorted(cpop, key=lambda x: x.getFitness())[idx:len(pop)]

def ElitismReplacement(pop, cpop):
	"""
	Take some small number of the best parents
	and keep them in place of the worst offspring
	(if they're better). Strengthens convergence,
	but may result in premature convergence.

	"""
	pop = sorted(pop, key=lambda x: x.getFitness())
	cpop = sorted(cpop, key=lambda x: x.getFitness())[::-1]

	# 10% of best parents might survive.
	idx = len(pop) / 10

	#Make sure we only replace with better children.
	bestparents = pop[:idx]
	worstchildren = cpop[:idx]
	newpop = sorted(pop + cpop, key=lambda x: x.getFitness())[:len(pop) - idx]
	for i in range(len(bestparents)):
		if bestparents[i].getFitness() < worstchildren[i].getFitness():
			newpop.append(bestparents[i])
		else:
			newpop.append(worstchildren[i])

	random.shuffle(newpop)
	return newpop

def TruncationReplacement(pop, cpop):
	"""
	 Take the best N from the union of parent and
	offspring populations. Very strong selection, 
	needs to be balanced with something else to avoid 
	premature convergence problems.

	"""
	foo = sorted(pop + cpop, key=lambda x: x.getFitness())[:len(pop)]
	random.shuffle(foo)
	return foo

def RandomReplacement(pop, cpop):

	sel = random.randint(1, 3)

	#GENERATIONAL NOT INCLUDED.
	#It always showed bad results, since it basically
	#premature converges the population at that point.
	#if sel  == 0:
	#	return GenerationalReplacement(pop, cpop)
	if sel == 1:
		return SteadyStateReplacement(pop, cpop)
	if sel == 2:
		return ElitismReplacement(pop, cpop)
	if sel == 3:
		return TruncationReplacement(pop, cpop)