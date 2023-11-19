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
            result: list[str]
            ) -> bool:

        arctic_map = [x.copy() for x in arctic_map]
        if not is_valid(x, y, arctic_map):
            return False

        if arctic_map[x][y] == "C":
            result.append(path)
            return True

        temp: str = arctic_map[x][y]
        arctic_map[x][y] = "X"

        for dx, dy, direction in [(0, 1, "R"), (1, 0, "D"), (0, -1, "L"), (-1, 0, "U")]:
            new_x, new_y = x + dx, y + dy
            new_path = path + [direction]

            if backtrack(new_x, new_y, new_path, arctic_map, result):
                return True

        arctic_map[x][y] = temp
        return False


def find_cub(arctic_map: list[list[str]]) -> list[str]:
    # Vytvoříme kopii mapy, abychom ji mohli v klidu modifikovat a nemenili puvodni
    arctic_map = [list(x) for x in arctic_map]
    result: list[str] = []
    start_x, start_y = 0, 0

    backtrack(start_x, start_y, [], arctic_map, result)

    if result:
        return result[0]
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