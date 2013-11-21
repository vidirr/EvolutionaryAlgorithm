Evolutionary Algorithms
=====================

##### Table of contents

1. [Introduction](#intro)
2. [Installation](#install)
3. [Running the program](#run)
4. [Configuration File](#config)


<a name="intro" />
##1. Introduction

The following code is written for a programming assignment at [Reykjavík University](http://www.ru.is) for the class T-504-ITML - Introduction to Machine Learning.
It focuses on implementing different EA algorithms, as well as different
approaches for solving them using crossovers, mutation, selection etc.

This code is published under the GNU GPL.

<a name="install" />
##2. Installation

Installing the suite is as simple as cloning the repo and running EA_main.py [name_of_test]. The example test configurations can be found inside [<code>config.ini</code>](https://github.com/vidirr/EvolutionaryAlgorithm/blob/master/config.ini).


<code>git clone https://www.github.com/vidirr/EvolutionaryAlgorithm</code>


<a name="run" />
##3. Running the program

The program is initiated from the commandline, where the name of the test to be run is passed as a argument.

<a name="config" />
##4 Configuration File
The configuration file is called [<code>config.ini</code>](https://github.com/vidirr/EvolutionaryAlgorithm/blob/master/config.ini). All tests are defined within that file. You can add multiple tests to [<code>config.ini</code>](https://github.com/vidirr/EvolutionaryAlgorithm/blob/master/config.ini), and then execute that test by passing the test name as an argument to the program.

Example configuration for a single test:
```ini
[f1_1]                                  ;Test name
POPULATION_SIZE = 100					;Population size
RANGE_MIN = -5.12                       ;Min range for test function
RANGE_MAX = 5.11                        ;Max range for test function
N = 1                                   ;Population size
TEST_FUNCTION = F1                      ;F1, F2, Shekel, Rana
ITERATIONS = 100                        ;Number of iterations
SELECTION_SCHEME = Tournament           ;Tournament, RankBiased,, Random
CROSSOVER_TYPE = TwoPoint               ;OnePoint, TwoPoint, Uniform, Random
MUTATION_RATE = 0.01                    ;Mutation rate
REPLACEMENT_METHOD = Generational       ;Generational, SteadyState, Elitism, Truncation, Random
MESSAGE = Solving De Jong F1 problem..
```