"""
	

"""
import random

def GenerationalReplacement(pop, cpop):
	"""
	Simply replaces the entire population with the new population.

	"""
	return cpop

def SteadyStateReplacement(pop, cpop):
	"""
	Fewer parents then offspring.
	Some parents always survive.

	"""
	idx = (len(pop)/10) * 4
	return sorted(pop, key=lambda x: x.getFitness())[:idx] + sorted(cpop, key=lambda x: x.getFitness())[idx:len(pop)]




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

	#print "Length: " + str(len(newpop)) + "\n"
	#mport time; time.sleep(1)
	return newpop


def TruncationReplacement(pop, cpop):
	"""
	 Take the best N from the union of parent and
	offspring populations. Very strong selection, 
	needs to be balanced with something else to avoid 
	premature convergence problems.

	"""
	foo = pop + cpop
	return sorted(foo, key=lambda x: x.getFitness())[:len(pop)]