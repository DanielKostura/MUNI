from math import log

with open("first.txt", 'r') as f:
    first_contents = f.read()
    first_lines = first_contents.split('\n')

first_entropy = 0

for line in first_lines:
    p = float(line.split(':')[1])
    if p == 0:
        continue
    first_entropy -= p*log(p, 2)

print(f"Entropy of first letters: {first_entropy}")

with open("last.txt", 'r') as f:
    last_contents = f.read()
    last_lines = last_contents.split('\n')

last_entropy = 0

for line in last_lines:
    p = float(line.split(':')[1])
    if p == 0:
        continue
    last_entropy -= p*log(p, 2)

print(f"Entropy of last letters: {last_entropy}")

max_entropy = 0

for i in range(26):
    p = 1/26
    max_entropy -= p*log(p,2)

print(f"Maximal possible entropy: {max_entropy}")