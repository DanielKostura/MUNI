def is_valid(
            x: int,
            y: int,
            arctic_map: list[list[str]]
            ) -> bool:

    return 0 <= x < len(arctic_map) and 0 <= y < len(arctic_map[0]) and arctic_map[x][y] != "X"


def backtrack(
            x: int,
            y: int,
            path: list[str],
            arctic_map: list[list[str]],
            result: list[str],
            count: int
            ) -> list[str]: #bool

    if count < len(arctic_map)*len(arctic_map[0]): # aby sa to nezacyklilo ked je v arctic_map cyklus
        if arctic_map[x][y] == 'C':
            result = path.copy()
            return result
        
        if len(result) == 0 and is_valid(x, y+1, arctic_map) and (len(path) == 0 or path[-1] != 'L'):
            path.append('R')
            result = backtrack(x, y+1, path, arctic_map, result, count + 1)
        
        if len(result) == 0 and is_valid(x, y-1, arctic_map) and (len(path) == 0 or path[-1] != 'R'):
            path.append('L')
            result = backtrack(x, y-1, path, arctic_map, result, count + 1)
        
        if len(result) == 0 and is_valid(x+1, y, arctic_map) and (len(path) == 0 or path[-1] != 'U'):
            path.append('D')
            result = backtrack(x+1, y, path, arctic_map, result, count + 1)
        
        if len(result) == 0 and is_valid(x-1, y, arctic_map) and (len(path) == 0 or path[-1] != 'D'):
            path.append('U')
            result = backtrack(x-1, y, path, arctic_map, result, count + 1)

        if path:
            path.pop()
        return result
    return result


def find_cub(arctic_map: list[list[str]]) -> list[str]:
    # Vytvoříme kopii mapy, abychom ji mohli v klidu modifikovat a nemenili puvodni
    arctic_map = [list(x) for x in arctic_map]
    result: list[str] = []
    start_x, start_y = 0, 0
    
    result = backtrack(start_x, start_y, [], arctic_map, result, 0)

    if result:
        return result
    else:
        return []

# testy:
arctic_map = [
    ["S", ".", ".", ".", "."],
    ["X", "X", "X", "X", "."],
    ["C", ".", ".", ".", "."]
]

path = find_cub(arctic_map)
print(path) # ['R', 'R', 'R', 'R', 'D', 'D', 'L', 'L', 'L', 'L']

arctic_map = [
    ["S", ".", ".", ".", "."],
    [".", "X", "X", "X", "X"],
    [".", "X", ".", ".", "."],
    [".", "X", ".", "X", "X"],
    [".", ".", ".", ".", "C"]
]

path = find_cub(arctic_map)
print(path) # ['D', 'D', 'D', 'D', 'R', 'R', 'R', 'R']

arctic_map = [
    ["S", ".", ".", ".", "."],
    [".", "X", "X", "X", "X"],
    [".", "X", ".", "X", "C"],
    [".", "X", ".", ".", "."],
    [".", "X", ".", ".", "X"]
]

path = find_cub(arctic_map)
print(path) # []

arctic_map = [
    [['S', '.', '.', '.', '.'], 
     ['.', '.', 'X', '.', 'X'], 
     ['.', 'X', '.', '.', '.'], 
     ['.', 'X', '.', 'X', 'X'], 
     ['.', '.', '.', '.', '.']]
]
path = find_cub(arctic_map)
print(path)
