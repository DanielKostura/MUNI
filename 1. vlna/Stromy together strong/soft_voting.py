def soft_voting(probability_distributions: list[list[float]]) -> list[float]:
    pole = []
    for i in range(len(probability_distributions[0])):
        sum = 0
        for j in range(len(probability_distributions)):
            sum += probability_distributions[j][i]

        pole.append(sum/len(probability_distributions))
    return pole

# Testy:
print(soft_voting([[0.5, 0.4, 0.1], [0.2, 0.5, 0.3], [0.4, 0.3, 0.3]]))  # [0.366666666, 0.4, 0.233333333333]
print(soft_voting([[0.1, 0.5, 0.4]]))
print(soft_voting([[0.5, 0.5], [0.1, 0.9], [0.3, 0.7]]))