import ConfigParser

config = ConfigParser.ConfigParser()
config.read('config.ini')


def get_config_for_test(string):
    """
    Returns a dict with the configuration values of the string
    thats sent in to the function.

    """

    return {'n': config.getint(string, 'N'),
            'range_min': config.getfloat(string, 'RANGE_MIN'),
            'range_max': config.getfloat(string, 'RANGE_MAX'),
            'test_function': config.get(string, 'TEST_FUNCTION'),
            'iterations': config.getint(string, 'ITERATIONS'),
            'crossover_type': config.get(string, 'CROSSOVER_TYPE'),
            'mutation_type': config.get(string, 'MUTATION_TYPE')}



def main():
    test = ['TEST1', 'TEST2', 'TEST3', 'TEST4',
            'TEST5', 'TEST6', 'TEST7', 'TEST8']
    for x in test:
        print get_config_for_test(x)


if __name__ == '__main__':
    main()
