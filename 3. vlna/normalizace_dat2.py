from typing import List

# Tuto funkci implementuj.
def minmax(values: List[float]) -> List[float]:
    mi = min(values)
    ma = max(values)

    for i in range(len(values)):
        values[i] = (values[i]-mi)/(ma-mi)
    return values
    

# Testy:
print(minmax([0, 1, 2, 3, 4, 5])) # [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
print(minmax([-20, 2, 10000])) # [0.0, 0.0021956087824351296, 1.0]
print(minmax([5, 6, 1, 4, 0])) # [0.8333333333333334, 1.0, 0.16666666666666666, 0.6666666666666666, 0.0]
