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
    node_3 = DecisionTreeNode(STOJACI_LUDIA, [True], [True, False])

    node_2 = DecisionTreeNode(TAZKY_BATOH, [True], [node_3, True])

    node_1 = DecisionTreeNode(
        VOLNE_MIESTA,
        [VOLNE_MIESTA_ZOPAR, VOLNE_MIESTA_VELA],
        [False, node_2, True],
        )
    
    return DecisionTree(node_1)

tree = make_decision_tree()
# [UNAVENY, TAZKY_BATOH, VZDIALENOST, STOJACI_LUDIA, VOLNE_MIESTA]
print("False 0", end=" - ")
print(
    tree.evaluate([False, True, VZDIALENOST_VIAC_AKO_2, True, VOLNE_MIESTA_ZIADNE])
)  # False 0

print("False 1", end=" - ")
print(
    tree.evaluate([True, False, VZDIALENOST_0_1, False, VOLNE_MIESTA_ZIADNE])
)  # False 1

print("True 2", end=" - ")
print(
    tree.evaluate([False, False, VZDIALENOST_VIAC_AKO_2, False, VOLNE_MIESTA_VELA])
)  # True 2

print("False 3", end=" - ")
print(
    tree.evaluate([True, True, VZDIALENOST_1_2, True, VOLNE_MIESTA_ZIADNE])
)  # False 3

print("True 4", end=" - ")
print(
    tree.evaluate([True, True, VZDIALENOST_0_1, True, VOLNE_MIESTA_ZOPAR])
)  # True 4

print("True 5", end=" - ")
print(
    tree.evaluate([True, True, VZDIALENOST_1_2, True, VOLNE_MIESTA_VELA])
)  # True 5

print("True 6", end=" - ")
print(
    tree.evaluate([False, True, VZDIALENOST_1_2, True, VOLNE_MIESTA_ZOPAR])
)  # True 6

print("True 7", end=" - ")
print(
    tree.evaluate([False, True, VZDIALENOST_1_2, False, VOLNE_MIESTA_VELA])
)  # True 7

print("True 8", end=" - ")
print(
    tree.evaluate([False, False, VZDIALENOST_1_2, False, VOLNE_MIESTA_ZOPAR])
)  # True 8

print("False 9", end=" - ")
print(
    tree.evaluate([False, False, VZDIALENOST_1_2, True, VOLNE_MIESTA_ZOPAR])
)  # False 9

