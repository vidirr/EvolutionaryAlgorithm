#! /usr/bin/env python2
from TestsFactory import Tests
from AlgorithmFactory import Algorithms
import sys
import ConfigParser

#    Returns a dict with the configuration values of the string
#    that's sent in to the function.

algs = Algorithms
t = Tests

def get_configuration(string):
    config = ConfigParser.ConfigParser()
    config.read('config.ini')

    return {
        'population_size' : config.getint(string, 'POPULATION_SIZE'),
        'n': config.getint(string, 'N'),
        'range_min': config.getfloat(string, 'RANGE_MIN'),
        'range_max': config.getfloat(string, 'RANGE_MAX'),
        'test_function': config.get(string, 'TEST_FUNCTION'),
        'iterations': config.getint(string, 'ITERATIONS'),
        'crossover_type': config.get(string, 'CROSSOVER_TYPE'),
        'selection_scheme' : config.get(string, 'SELECTION_SCHEME'),
        'mutation_type': config.get(string, 'MUTATION_TYPE')
    }

def F1(N, popsize, iters, xmin, xmax, crossover, selection):
	print "Solving De Jong F1 problem.."
	return algs.BEA(N=N, popsize=popsize, xmin=xmin, xmax=xmax, test=t.f1,iters=iters, crossover=crossover, selection = selection)

def F2(N, popsize, iters, xmin, xmax, crossover, selection):
	print "Solving De Jong F2 problem.."
	return algs.BEA(N=N, popsize=popsize, xmin=xmin, xmax=xmax, test=t.f2, iters=iters, crossover=crossover, selection = selection)

def Shekel(N, popsize, iters, xmin, xmax, crossover, selection):
	print "Solving Shekel's Foxholes problem.."
	return algs.BEA(N=N, popsize=popsize, xmin=xmin, xmax=xmax, test=t.shekel, iters=iters, crossover=crossover, selection = selection)

def Rana(N, popsize, iters, xmin, xmax, crossover, selection):
	print "Solving Rana's function problem.."
	return algs.BEA(N=N, popsize=popsize, xmin=xmin, xmax=xmax, test=t.rana, iters=iters, crossover=crossover, selection = selection)

tests = {
    'F1' : F1,
    'F2' : F2,
    'Rana' : Rana,
    'Shekel' : Shekel,
}

def main():
	#Parsing command line arguments for now..
    #We accept a single argument which is a reference to TESTx found in config.ini
	if(len(sys.argv) > 1):
		prob = sys.argv[1]
	else:
		prob = "TEST3"

    #Read algorithm configuration from cfg file.
	cfg = get_configuration(prob)

    #The function name is read from the cfg file and mapped using an associative array
    #Other parameters for the current test are then also read from the cfg file.
	ans = tests[cfg['test_function']](
        N = cfg['n'],
        popsize = cfg['population_size'],
        iters = cfg['iterations'],
        xmin = cfg['range_min'],
        xmax = cfg['range_max'],
        crossover = cfg['crossover_type'],
        selection = cfg['selection_scheme'])

        print "Iteration {0}/{1}".format(cfg['iterations'], cfg['iterations'])

        print ans

if __name__ == "__main__":
	main()