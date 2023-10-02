# Vytvorte funkci na vypocet kvadraticke rovnice.
# Smazte prikaz `return None` a piste svuj program.
def solve(a: float, b: float, c: float) -> float:
    discriminant = b**2 - 4*a*c

    if discriminant < 0:
        return None 
    
    elif discriminant == 0:
        result = -b / (2 * a)
        return result
    
    else:
        discriminant = discriminant ** 0.5
        result1 = (-b + discriminant) / (2 * a)
        result2 = (-b - discriminant) / (2 * a)
        
        if result1 < result2:
            return result2
        else:
            return result1

# priklady volani:
print(solve(2, -11, 14))  # 3.5
print(solve(1, 2, -63))  # 7.0
print(solve(1, 3, 7))  # None
