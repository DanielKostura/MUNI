from math import sqrt

def corr_coef(data):
    n = len(data)
    sum_x = sum(x for x, y in data)
    sum_y = sum(y for x, y in data)
    sum_xy = sum(x * y for x, y in data)
    sum_x_squared = sum(x**2 for x, y in data)
    sum_y_squared = sum(y**2 for x, y in data)

    numerator = n * sum_xy - sum_x * sum_y
    denominator = sqrt((n * sum_x_squared - sum_x**2) * (n * sum_y_squared - sum_y**2))

    correlation_coefficient = numerator / denominator
    return correlation_coefficient

# Testy:
data1 = [
    (0, 0), (1, -1), (1, 1)
]

data2 = [
    (0, 0), (1, 1), (2, -2), (3, 3), (4, -4)
]

data3 = [
    (0, 0), (0, 0), (0, 0), (0, 0), (0, 0),
    (0, 0.5), (0, 0.5), (0, 0.5), (0, 0.5), (0, 0.5),
    (1, 0.5), (1, 0.5), (1, 0.5), (1, 0.5), (1, 0.5),
    (4, 2), (4, 2), (4, 2), (4, 2), (4, 2)
    ]

data4 = [
    (0, 0), (1, 0.5), (4, 2)
    ]


print(corr_coef(data1))  # 0.0
print(corr_coef(data2))  # -0.3511234415883917
print(corr_coef(data3))  # 0.9658242787731629
print(corr_coef(data4))  # 1.0