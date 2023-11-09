from typing import List, Dict

data = load_wine()

COLORING = Dict[str, str]
COUNTRIES = List['Country']


class Country:
    name: str
    neighbors: List[str]

    def __init__(self, name: str, neighbors: List[str]):
        self.name = name
        self.neighbors = neighbors


def is_ok(coloring: COLORING, countries: COUNTRIES) -> bool:
    # TODO
    pass


def is_final(
    coloring: COLORING, # slovník název státu : barva.
    countries: COUNTRIES,
    country_index: int # je pomocná proměnná, která označuje index státu, který právě obarvujeme
) -> bool:
    # TODO
    pass


def solve_coloring(
    coloring: COLORING, # slovník název státu : barva.
    countries: COUNTRIES,
    colors: List[str], # seznam dostupných barev
    country_index: int = 0 # je pomocná proměnná, která označuje index státu, který právě obarvujeme
) -> bool:
    if not is_ok(coloring, countries):
        return False

    if is_final(coloring, countries, country_index):
        print(coloring)
        return True

    for color in colors:
        coloring[countries[country_index].name] = color
        if solve_coloring(coloring, countries, colors, country_index+1):
            return True

    return False


# Testy:
coloring: COLORING = {}
countries = [
    Country('El Sobov', ['La Losov']),
    Country('La Losov', ['El Sobov']),
]
print(solve_coloring(coloring, countries, ['RED', 'GREEN']))
