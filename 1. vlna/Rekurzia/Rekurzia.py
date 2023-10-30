from typing import List

# Tuto funkci implementuj.
def seat_permutations(friends: List[str]):
    if len(friends) <= 1:
        return [friends]
    
    permutacie = []
    for i in range(len(friends)):
        zvysok = friends[:i] + friends[i+1:]
        for perm in seat_permutations(zvysok):
            permutacie.append([friends[i]] + perm)
    
    return permutacie

# Testy:
print(seat_permutations(["Karlik","Karlos", "Aida"]))  # [['Karlik', 'Karlos', 'Aida'], ['Karlik', 'Aida', 'Karlos'], ['Karlos', 'Karlik', 'Aida'], ['Karlos', 'Aida', 'Karlik'], ['Aida', 'Karlik', 'Karlos'], ['Aida', 'Karlos', 'Karlik']]
