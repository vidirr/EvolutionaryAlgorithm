__author__ = 'GSUS'

import ConfigParser

config = ConfigParser.ConfigParser()
config.read('config.ini')

n = config.getint('BEA', 'N')
range_min = config.getfloat('BEA', 'RANGE_MIN')
range_max = config.getfloat('BEA', 'RANGE_MAX')
test_function = config.get('BEA', 'TEST_FUNCTION')
iterations = config.getint('BEA', 'ITERATIONS')
selection_scheme = config.get('BEA', 'SELECTION_SCHEME')
crossover_type = config.get('BEA', 'CROSSOVER_TYPE')
mutation_type = config.get('BEA', 'MUTATION_TYPE')


print "N =",n
print "Range(",range_min,",",range_max,")"
print "Test function = ",test_function
print "Iterations =",iterations
print "Selection Scheme = ", selection_scheme
print "Crossover Type = ", crossover_type
print "Mutation Type = ", mutation_type

def f1():
    print "F1"
def f2():
    print "F2"
def shekel():
    print "Shekel"
def rana():
    print "rana"

test_functions = {
    "F1" : f1,
    "F2" : f2,
    "Shekel" : shekel,
    "Rana" : rana,
}

selection_schemes = {
    "Roulette" : RouletteWheelSelection,
    "Tournament" : TournamentSelection,
    "RankBiased" : RankBiasedSelection,
}

crossover_types = {
    "OnePoint" : OnePointCrossover,
}

mutation_types = {
    "Whatever" : Whatever
}