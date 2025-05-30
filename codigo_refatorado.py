import random
import numpy as np
import time
import statistics
from typing import List, Tuple


class GeneticAlgorithmKnapsack:
    def __init__(
        self,
        weights: List[int],
        values: List[int],
        capacity: int,
        pop_size: int = 100,
        generations: int = 100,
        mutation_rate: float = 0.01,
        tournament_size: int = 3
    ):
        self.weights = weights
        self.values = values
        self.capacity = capacity
        self.pop_size = pop_size
        self.generations = generations
        self.mutation_rate = mutation_rate
        self.tournament_size = tournament_size
        self.n_items = len(weights)

    def initialize_population(self) -> List[List[int]]:
        return [np.random.randint(0, 2, self.n_items).tolist() for _ in range(self.pop_size)]

    def fitness(self, solution: List[int]) -> float:
        total_weight = sum(w * s for w, s in zip(self.weights, solution))
        total_value = sum(v * s for v, s in zip(self.values, solution))

        if total_weight > self.capacity:
            return -total_weight  # Penalização
        return total_value

    def tournament_selection(self, population: List[List[int]], fitnesses: List[float]) -> List[int]:
        tournament = random.sample(range(len(population)), self.tournament_size)
        winner_idx = max(tournament, key=lambda i: fitnesses[i])
        return population[winner_idx]

    def crossover(self, parent1: List[int], parent2: List[int]) -> Tuple[List[int], List[int]]:
        point1 = random.randint(1, self.n_items - 2)
        point2 = random.randint(point1, self.n_items - 1)
        child1 = parent1[:point1] + parent2[point1:point2] + parent1[point2:]
        child2 = parent2[:point1] + parent1[point1:point2] + parent2[point2:]
        return child1, child2

    def mutate(self, solution: List[int]) -> List[int]:
        return [
            1 - s if random.random() < self.mutation_rate else s
            for s in solution
        ]

    def run(self) -> Tuple[List[int], float, float]:
        population = self.initialize_population()

        for _ in range(self.generations):
            fitnesses = [self.fitness(ind) for ind in population]
            new_population = []

            best_idx = np.argmax(fitnesses)
            new_population.append(population[best_idx])

            while len(new_population) < self.pop_size:
                parent1 = self.tournament_selection(population, fitnesses)
                parent2 = self.tournament_selection(population, fitnesses)
                child1, child2 = self.crossover(parent1, parent2)
                child1 = self.mutate(child1)
                child2 = self.mutate(child2)
                new_population.extend([child1, child2])

            population = new_population[:self.pop_size]

        fitnesses = [self.fitness(ind) for ind in population]
        best_idx = np.argmax(fitnesses)
        best_solution = population[best_idx]
        best_value = fitnesses[best_idx]
        best_weight = sum(w * s for w, s in zip(self.weights, best_solution))

        return best_solution, best_value, best_weight
