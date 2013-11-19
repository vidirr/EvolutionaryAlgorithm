#! /usr/bin/env python2
from AlgorithmFactory import Algorithms
import sys
import ConfigParser
import stats
#    Returns a dict with the configuration values of the string
#    that's sent in to the function.

algs = Algorithms

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
        'mutation_rate': config.getfloat(string, 'MUTATION_RATE'),
        'replacement_method': config.get(string, 'REPLACEMENT_METHOD'),
        'message' : config.get(string, 'MESSAGE')
    }

def main():
	#Parsing command line arguments for now..
    #We accept a single argument which is a reference to TESTx found in config.ini
	if(len(sys.argv) > 1):
		prob = sys.argv[1]
	else:
		prob = "f2_2"

    #Read algorithm configuration from cfg file.
	cfg = get_configuration(prob)
        for att in cfg:
            print "{0} = {1}".format(str(att).upper(), cfg[att])

    #The function name is read from the cfg file and mapped using an associative array
    #Other parameters for the current test are then also read from the cfg file.
	#reslist = []
	#for i in xrange(0,30):
            ans = algs.BEA(N = cfg['n'], popsize = cfg['population_size'], xmin = cfg['range_min'], xmax = cfg['range_max'],
                testfunc = cfg['test_function'], iters = cfg['iterations'], crossover = cfg['crossover_type'],
                selection = cfg['selection_scheme'], mutation = cfg['mutation_rate'], replacement = cfg['replacement_method'])

            print "Iteration {0}/{1}".format(cfg['iterations'], cfg['iterations'])

            print ans
            #reslist.append(ans.getFitness())

        #print "StdDev: ", stats.stdev(reslist)
        #print "Mean: ", stats.mean(reslist)

if __name__ == "__main__":
	main()