"""
NOT YET IMPLEMENTED
This class will extend the GeneticAlgorithm class. Main functions will be to test a simple implementation of the base
GeneticAlgorithm class and debug it. The class will evolve a set of random strings to approximate as closely as possible
a given "perfect" string.
"""

from GeneticAlgorithm import GeneticAlgorithm


class StringGA(GeneticAlgorithm):

    def __init__(self, sample_string="Monty"):

        self._ascii_dict = {i: chr(i) for i in range(129)}

        GeneticAlgorithm.__init__(self, pop_size=100, chrom_len=len(sample_string), g_size=len(self._ascii_dict))
