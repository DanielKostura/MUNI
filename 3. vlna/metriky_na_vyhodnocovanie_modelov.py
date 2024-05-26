from typing import List, Tuple


# Túto funkciu implementuj.
def f1score(points: List[Tuple[float, float]], radius: float) -> float:
    tp, tn, fp, fn = 0, 0, 0, 0
    
    for x, y in points:
        if x**2 + y**2 <= radius**2 and 3*x**2 +5*y**2 <= 400:
            tp += 1

        elif x**2 + y**2 >= radius**2 and 3*x**2 +5*y**2 >= 400:
            tn += 1
        
        elif x**2 + y**2 <= radius**2 and 3*x**2 +5*y**2 >= 400:
            fp += 1
        
        elif x**2 + y**2 >= radius**2 and 3*x**2 +5*y**2 <= 400:
            fn += 1

    recall = tp/(tp+fn)
    precision = tp/(tp+fp)

    return 2*(precision*recall)/(precision+recall)


example_points = [(1, 1), (4, 3), (-10, 3), (-8, -7), (3, -9)]
print(f1score(example_points, 10))  # 0.6666666666666666