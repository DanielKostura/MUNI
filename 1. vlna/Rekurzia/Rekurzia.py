from typing import List

pole = []
def seat_permutations(friends: List[str]) -> List[List[str]]:
    if len(pole) == len(friends):
        return pole

    else:
        pole.append(friends)
        print(pole)
        seat_permutations(friends)


# Testy:
print(seat_permutations(["Karlik","Karlos"]))  # [['Karlik', 'Karlos'], ['Karlos', 'Karlik']]