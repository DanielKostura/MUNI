import math
prve_pismena = [0.0927, 0.0592, 0.0158, 0.0592 ,0.0473 ,0.0316 ,0.0316 ,0.0296 ,0.0434 ,0.0513 ,0.0493 ,0.075 ,0.0848 ,0.0256 ,0.0178 ,0.0178 ,0.0 ,0.075 ,0.069 ,0.0178 ,0.0039 ,0.0671 ,0.0 ,0.002 ,0.0 ,0.0335]
posledne_pismena = [0.86, 0.0, 0.0, 0.0039, 0.1045, 0.0, 0.0, 0.0, 0.002, 0.0, 0.0, 0.0039, 0.002, 0.0118, 0.0, 0.0, 0.0, 0.0039, 0.0039, 0.0039, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

entropy = 0
for i in range(0, len(prve_pismena)):
    if prve_pismena[i] != 0:
        entropy += prve_pismena[i] * math.log2(1/prve_pismena[i])
        print(f"{prve_pismena[i]} * {math.log2(1/prve_pismena[i])} = {prve_pismena[i] * math.log2(1/prve_pismena[i])}")

print(entropy)
entropy = 0

for i in range(0, len(posledne_pismena)):
    if posledne_pismena[i] != 0:
        entropy += posledne_pismena[i] * math.log2(1/posledne_pismena[i])
        print(f"{posledne_pismena[i]} * {math.log2(1/posledne_pismena[i])} = {posledne_pismena[i] * math.log2(1/posledne_pismena[i])}")

print(entropy)