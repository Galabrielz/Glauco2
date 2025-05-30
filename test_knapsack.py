import pytest
from codigo_refatorado import GeneticAlgorithmKnapsack


def test_small_dataset():
    weights = [2, 3, 4, 5]
    values = [3, 4, 5, 6]
    capacity = 5

    ga = GeneticAlgorithmKnapsack(weights, values, capacity, generations=50)
    solution, value, weight = ga.run()

    assert weight <= capacity
    assert value >= 6  # Espera-se pelo menos algum valor válido


def test_large_dataset():
    import numpy as np
    weights = np.random.randint(1, 100, 100).tolist()
    values = np.random.randint(1, 100, 100).tolist()
    capacity = 500

    ga = GeneticAlgorithmKnapsack(weights, values, capacity, generations=50)
    solution, value, weight = ga.run()

    assert weight <= capacity
    assert value > 0
