"""
NOT YET IMPLEMENTED
This class will extend the GeneticAlgorithm class. Main functions will be override how the chromosomes are encoded and
create a fitness function that tests the chromosome when compared to classical baroque melodic rules.
"""

from GeneticAlgorithm import GeneticAlgorithm


class MusicGA(GeneticAlgorithm):

    def __init__(self, pop_size=10, chrom_len=10, g_size=11):
        GeneticAlgorithm.__init__(self, pop_size, chrom_len, g_size)
