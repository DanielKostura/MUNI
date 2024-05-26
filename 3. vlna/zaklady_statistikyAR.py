def expected_value(probability: dict[float, float]) -> float:
    return sum(x * px for x, px in probability.items())


def variance(probability: dict[float, float]) -> float:
    ex = expected_value(probability)
    return sum((x - ex)**2 * px for x, px in probability.items())


def corr_coef(data: list[tuple[float, float]]) -> float:
    probability = {}
    for (x, y) in data:
        probability[(x,y)] = probability.get((x,y), 0) + 1
    
    length = len(data)
    for ((x,y), p) in probability.items():
        probability[(x,y)] = p / length
    
    probability_x = {}
    probability_y = {}
    for ((x,y), p) in probability.items():
        probability_x[x] = probability_x.get(x, 0) + p
        probability_y[y] = probability_y.get(y, 0) + p
    
    ex = expected_value(probability_x)
    ey = expected_value(probability_y)

    variance_x = variance(probability_x)
    variance_y = variance(probability_y)
    deviation_x = sqrt(variance_x)
    deviation_y = sqrt(variance_y)

    covariance = sum((x - ex) * (y - ey) * pxy for ((x,y), pxy) in probability.items())
    correlation_coefficient = covariance / (deviation_x * deviation_y)
    return correlation_coefficient