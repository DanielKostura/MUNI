class Node:
    def __init__(self, data=None):
        self.data = data
        self.children = []

    def add_child(self, child):
        self.children.append(child)

# Tuto funkci implementuj.
def tree_depth(node: Node, level = 0) -> int:
    current_lvl = 0
    if len(node.children) > 0:
        for child in node.children:
            current_lvl = 1
            current_lvl += tree_depth(child)
            if current_lvl > level:
                level = current_lvl

        return level
    return current_lvl

# Testy:
g_subtree = Node('G')
g_subtree.add_child(Node('H'))
g_subtree.add_child(Node('I'))

c_subtree = Node('C')
c_subtree.add_child(g_subtree)

b_subtree = Node('B')
b_subtree.add_child(Node('D'))
b_subtree.add_child(Node('E'))
b_subtree.add_child(Node('F'))

tree = Node('A')
tree.add_child(b_subtree)
tree.add_child(c_subtree)

print(tree_depth(tree))  # 3