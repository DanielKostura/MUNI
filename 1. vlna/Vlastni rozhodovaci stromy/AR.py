def make_decision_tree() -> 'DecisionTree': # Ovocie
    node1 = DecisionTreeNode(2, [2], [False, True])
    node2 = DecisionTreeNode(2, [1], [False, True])
    root = DecisionTreeNode(1,[True], [node2, node1])
    return DecisionTree(root)

def make_decision_tree() -> 'DecisionTree': # Sacharidy
    node1 = DecisionTreeNode(0, [5], [True, False])
    node2 = DecisionTreeNode(0, [2], [True, False])
    root = DecisionTreeNode(2, [1, 2], [node2, node1, True])
    return DecisionTree(root)

def make_decision_tree() -> 'DecisionTree': # Zelenina
    node4 = DecisionTreeNode(0, [2], [True, False])
    node3 = DecisionTreeNode(0, [7], [True, False])
    node2 = DecisionTreeNode(2, [2], [node3, True])
    node1 = DecisionTreeNode(2, [1], [False, node4])
    root = DecisionTreeNode(1, [True], [node2, node1])
    return DecisionTree(root)

def make_decision_tree() -> 'DecisionTree': # Lolko
    node3 = DecisionTreeNode(1, [True], [False, True])
    node2 = DecisionTreeNode(2, [1], [False, True])
    node1 = DecisionTreeNode(2, [2], [node3, True])
    root = DecisionTreeNode(0, [15, 30, 45], [False, node1, node2, True])
    return DecisionTree(root)