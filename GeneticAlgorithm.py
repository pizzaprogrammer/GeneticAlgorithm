"""
A simple implementation of a Genetic Algorithm.
Copyright (c) 2019 Marco Costa
"""


from random import randrange
import pandas as pd


class GeneticAlgorithm(object):

    def __init__(self, pop_size=100, chrom_len=10, g_size=11):
        """
        Creates a GeneticAlgorithm object and Initializes our first generation population of chromosomes that all have
        randomly generated integer type genes.
        :param pop_size: the size of the entire population.
        :param chrom_len: how many genes are in a chromosome. (eg strand of DNA)
        :param g_size: how many possibilities are held within each gene. Value is n-1  (eg. for human DNA this number would be 3)
        """

        # Initializing class variables and constants.
        self._POPULATION_SIZE = pop_size
        self._CHROMOSOME_LENGTH = chrom_len
        self._GENE_SIZE = g_size
        self._FINAL_GENERATION = 1
        self._mating_population = pd.DataFrame(columns=['chromosome', 'fitness'], index=range(0, pop_size))
        self.population = pd.DataFrame(columns=['chromosome', 'fitness'], index=range(0, pop_size))

        # Initialize Generation 0 population.
        self._init_pop(pop_size, chrom_len, g_size)



    def _init_pop(self, pop_size, chrom_len, g_size):
        """
        This function is in charge of initializing the first generation with randomly generated chromosomes.
        When creating application specific child classes, this function should be overridden.
        :param pop_size: size of the entire population.
        :param chrom_len: how many genes are in a chromosome.
        :param g_size: how many possibilities are held within each gene.
        :return: none.
        """

        for i in range(pop_size):
            temp_gene = []
            for c in range(chrom_len):
                temp_gene.append(randrange(g_size))
            self.population['chromosome'][i] = temp_gene

        self._fitness()

    def __str__(self):
        """
        Makes it possible to print the entire GeneticAlgorithm object.
        :return: the entire population DataFrame cast as a string
        """

        return str(self.population)

    def _fitness(self):
        """
        Simple placeholder fitness function that determines fitness based on the value of the sum of all genes.
        This function is designed to be overridden by child classes as it's main use is just to test and make sure the
        other functions of the class function as expected.
        """

        for i in range(self._POPULATION_SIZE):
            self.population['fitness'][i] = sum(self.population['chromosome'][i])

    def _sort_population(self):
        """
        Sorts the population according to fitness in descending order.
        :return:
        """

        self.population = self.population.sort_values('fitness', ascending=False)
        self.population = self.population.reset_index(drop=True)

    def evolve(self, gen=1):
        """
        This function will evolve the entire population to the specified number of generations.
        :param gen: how many generations will the genetic algorithm evolve.
        :return: none.
        """

        self._FINAL_GENERATION = gen
        for i in range(gen):
            self._mate()

        self._sort_population()

    def _mating_pool(self):
        """
        The purpose of this function is to create a temporary dataframe where a mating pool is chosen from the existing
        population using a version of natural selection that weighs the chance of being selected based on the
        chromosomes fitness value. This function is not yet implemented. As it stands now, all members of n population
        mate in order to make n+1 generation.
        :return: none.
        """

        max_fitness = self.population['fitness'][0]
        mate_i = 0
        pop_i = 0
        while mate_i < self._POPULATION_SIZE:
            if self.population['fitness'][pop_i] >= randrange(max_fitness):
                self._mating_population['chromosome'][mate_i] = self.population['chromosome'][pop_i]
                self._mating_population['fitness'][mate_i] = self.population['fitness'][pop_i]
                pop_i += 1
                mate_i += 1
            else:
                pop_i += 1

            if pop_i == self._POPULATION_SIZE:
                pop_i = 0

        self.population = self._mating_population

    def _mate(self):
        """
        This function just calls the functions necessary to evolve each generation. As added functionality is added
        to the GA's evolution process, this function can added to. Also, child classes can easily override this function
        if they add functionality to the evolutionary process.
        :return: none.
        """
        self._mating_pool()
        self._sort_population()
        self._crossover()
        # The number passed in the mutate function represents the percent chance of a mutation occurring.
        self._mutate(50)
        self._fitness()

    def _crossover(self):
        """
        Neighboring chromosomes are chosen to mate. A random spot in the chromosomes is chosen and then the chromosomes
        exchange DNA at that break point. The resulting two chromosomes are the children for the next generation.
        :return: none. The population dataframe is directly modified.
        """
        i = 0
        while i < self._POPULATION_SIZE:
            cross_pos = randrange(self._CHROMOSOME_LENGTH)
            temp_chrom1 = self.population['chromosome'][i][cross_pos:] + \
                          self.population['chromosome'][i+1][:cross_pos]
            temp_chrom2 = self.population['chromosome'][i+1][cross_pos:] + \
                          self.population['chromosome'][i][:cross_pos]
            self.population['chromosome'][i] = temp_chrom1
            self.population['chromosome'][i+1] = temp_chrom2
            i += 2

    def _mutate(self, mutation_chance):
        """
        If a mutation occurs, one randomly chosen gene inside one randomly chosen chromosome will be replaced with
        a randomly generated gene.
        :param mutation_chance: the number passed here represents the percentage chance of a mutation 0-100
        :return: none.
        """
        if mutation_chance >= randrange(100):
            self.population['chromosome'][randrange(self._POPULATION_SIZE)][randrange(self._CHROMOSOME_LENGTH)] = \
                randrange(self._GENE_SIZE)

# The following functions are just simple getter functions for class variables.

    def get_pop_size(self):
        return self._POPULATION_SIZE

    def get_chrom_length(self):
        return self._CHROMOSOME_LENGTH

    def get_final_gen(self):
        return self._FINAL_GENERATION

    def get_gene_size(self):
        return self._GENE_SIZE
