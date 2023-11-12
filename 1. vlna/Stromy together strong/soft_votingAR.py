def soft_voting(probability_distributions: list[list[float]]) -> list[float]:
    return [sum(col) / len(probability_distributions) for col in
    zip(*probability_distributions)]