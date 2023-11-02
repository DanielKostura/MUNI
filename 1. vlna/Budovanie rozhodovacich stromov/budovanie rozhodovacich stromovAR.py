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

def make_decision_tree() -> "DecisionTree":
    node_1 = DecisionTreeNode(STOJACI_LUDIA, [True], [True, False])
    node_2 = DecisionTreeNode(TAZKY_BATOH, [True], [node_1, True])
    node_3 = DecisionTreeNode(VOLNE_MIESTA, [VOLNE_MIESTA_ZOPAR, VOLNE_MIESTA_VELA], [False, node_2, True])
    return DecisionTree(node_3)