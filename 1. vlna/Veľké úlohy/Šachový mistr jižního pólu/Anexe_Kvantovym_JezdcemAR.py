KNIGHT_MOVES = [(2, 1), (1, 2), (-1, 2), (-2, 1),
                (-2, -1), (-1, -2), (1, -2), (2, -1)]
SPLIT_MOVES = [(a, b) for a in KNIGHT_MOVES for b in KNIGHT_MOVES if a != b]

Moves = dict[tuple[int, int], list[tuple[tuple[int, int], tuple[int, int]]]]


class QKnight():
    board: list[list[int]]
    path: list[str]
    size: int
    moved: list[tuple[int, int]]

    def __init__(self, size: int) -> None:
        self.board = [[0] * size for _ in range(size)]
        self.path = []
        self.size = size
        self.moved = []

    def solve(self, x: int, y: int) -> bool:
        # Inicializujeme prvniho kone
        self.board[x][y] = True
        # Pro vizualizaci
        self.start = (x, y)
        # Zavolame backtracking funkci
        return self._backtracking(1)

    def _backtracking(self, existing_pieces: int) -> bool:
        # Pokud uz je pocet konu na sachovnici vetsi nebo rovno poctu policek na sachovnici
        # tak vrat True, jelikoz uz jsme projeli celou sachovnici
        if existing_pieces >= self.size ** 2:
            return True

        valid_moves = self._getValidMoves()

        for start in valid_moves.keys():
            # Pokud jsme s timhle konem jiz pohli, tak pokracujeme na dalsiho
            if start in self.moved:
                    continue
            # Vybereme start odkud budeme generovat dalsi kone
            for (end1, end2) in valid_moves[start]:
                # Vezmeme souradnice kam se mame pohnout
                x1, y1 = end1
                x2, y2 = end2
                self.board[x1][y1] = True
                self.board[x2][y2] = True

                # Ulozime position kone do listu moved, aby jsme vedeli ze jsme s tim jiz pohli
                self.moved.append(start)
                # Zapiseme do path v spravnem formatu
                self._writeMove(start, end1, end2)
                # Zavolame rekurzivne znovu funkci s navysenim o dva, jelikoz kazdy pohyb
                # rozdvoji dva dalsi kone
                if self._backtracking(existing_pieces + 2):
                    return True

                # Pokud se move nezdaril odebereme kone z listu moved jelikoz jsme s nim nebohli
                self.moved.pop()

                # Pokud se move nepodaril tak ho oddelame z path a smazeme dane kone z boardu
                self.path.pop()

                self.board[x1][y1] = False
                self.board[x2][y2] = False

        return False

    def _getValidMoves(self) -> Moves:
        # Generovani vsech moznych pohybu na sachovnici pro vsechny kone
        res = {}
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j]:
                    moves = self._getChildrenOfPiece(i, j)
                    if len(moves) > 0:
                        res[(i, j)] = moves
        return res

    def _getChildrenOfPiece(self, i: int, j: int) -> list[tuple[tuple[int, int], tuple[int, int]]]:
        # Generovani kombinaci moznych rozmnozeni kone
        allMoves = [(
                (x1 + i, y1 + j),
                (x2 + i, y2 + j)
            ) for ((x1, y1), (x2, y2)) in SPLIT_MOVES 
        ]
        return [(x,y) for (x,y) in allMoves if self._isMoveValid(x, y)]

    def _isMoveValid(self, newPos1: tuple[int, int], newPos2: tuple[int, int]) -> bool:
        x1, y1 = newPos1
        x2, y2 = newPos2
        # Jednoducha kontrola jestli je pohyb vubec mozny, je tam volno a je to v ramci board?
        if min(x1, x2, y1, y2) < 0 or max(x1, x2, y1, y2) >= self.size:
            return False
        if self.board[x1][y1] or self.board[x2][y2]:
            return False
        return True

    def _writeMove(self, start: tuple[int, int], pos1: tuple[int, int], pos2: tuple[int, int]) -> None:
        # Zapis algebraic chess notation do path, konverze pozic v listu na pozice k sachovnici
        notation = f"{chr(ord('a') + start[0]) + str(int(start[1])+1)}qK"

        notation += chr(ord("a") + pos1[0]) + str(int(pos1[1]+1)) + "&"\
                 + chr(ord("a") + pos2[0]) + str(int(pos2[1]+1))

        self.path.append(notation)



def play(size: int, start_pos: str) -> list[str] | None:
    # Pokud je board sudy tak nejde projit, jelikoz mame vzdy liche pocty konu
    # 1 + 2 = 3 + 2 = 5 ....
    if size % 2 == 0:
        return None

    start_pos = start_pos[2:]
    x,y = (ord(start_pos[0]) - ord('a'), int(start_pos[1]) - 1)
    if min(x, y) < 0 or max(x, y) >= size:
        return None

    q_knight = QKnight(size)
    if not q_knight.solve(x, y):
        return None

    return q_knight.path

print(play(5, "qKa1"))