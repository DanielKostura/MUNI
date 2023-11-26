from typing import List, Any, Union

UNAVENY = 0
TAZKY_BATOH = 1
VZDIALENOST = 2
STOJACI_LUDIA = 3
VOLNE_MIESTA = 4

VZDIALENOST_0_1 = 0
VZDIALENOST_1_2 = 1
VZDIALENOST_VIAC_AKO_2 = 2

VOLNE_MIESTA_ZIADNE = 0
VOLNE_MIESTA_ZOPAR = 1
VOLNE_MIESTA_VELA = 2


class DecisionTreeNode:
    def __init__(
        self,
        attribute: int,
        thresholds: List[Any],
        descendants: List[Union["DecisionTreeNode", bool]],
    ):
        self.attribute = attribute
        self.thresholds = thresholds
        self.descendants = descendants

    def evaluate(self, data: List[Any]) -> bool:
        value = data[self.attribute]
        for i in range(len(self.thresholds)):
            if value < self.thresholds[i]:
                if self.descendants[i] == True or self.descendants[i] == False:
                    return self.descendants[i]
                return self.descendants[i].evaluate(data)
        if self.descendants[-1] == True or self.descendants[-1] == False:
            return self.descendants[-1]
        return self.descendants[-1].evaluate(data)


class DecisionTree:
    def __init__(self, first_node):
        self.first_node = first_node

    def evaluate(self, data: List[Any]) -> bool:
        return self.first_node.evaluate(data)


# Tuto funkci implementuj.
def make_decision_tree() -> "DecisionTree":
    pass


# Príklad stromu, ktorý rozhodne si sadnúť v MHD,
# ak je Los unavený a zároveň je vzdialenosť presne 1-2
# (tento ukážkovy strom nevracá správne hodnoty pre celú tabuľku,
#  je tu len ako ukážka zápisu)
def make_example_tree() -> DecisionTree:
    # Uzol rozhoduje poďla atribútu vzdialenost,
    # hranice má na hodnotách 1-2 a >2,
    # pod hranicou 1-2 vráti False, medzi nimi wráti True a nad >2 vráti False
    node_1 = DecisionTreeNode(
        VZDIALENOST,
        [VZDIALENOST_1_2, VZDIALENOST_VIAC_AKO_2],
        [False, True, False],
    )

    # Uzol rozhoduje poďla atribútu unavený,
    # hranica je na hodnote True,
    # teda pre False, sa vráti False a pre True sa ide do node_1
    node_2 = DecisionTreeNode(UNAVENY, [True], [False, node_1])

    return DecisionTree(node_2)


tree = make_example_tree()
# [UNAVENY, TAZKY_BATOH, VZDIALENOST, STOJACI_LUDIA, VOLNE_MIESTA]
print(
    tree.evaluate(
        [False, True, VZDIALENOST_VIAC_AKO_2, True, VOLNE_MIESTA_ZIADNE]
    )
)  # False
print(
    tree.evaluate([True, True, VZDIALENOST_1_2, True, VOLNE_MIESTA_VELA])
)  # True
print(
    tree.evaluate([False, False, VZDIALENOST_1_2, True, VOLNE_MIESTA_ZOPAR])
)  # False