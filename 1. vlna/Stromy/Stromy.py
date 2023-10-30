# Trieda Node reprezentuje uzol stromu. Drží jeho dáta a zoznam potomkov
class Node:
    # Skonštruuje uzol s dátami
    def __init__(self, data=None):
        self.data = data
        self.children = []

    # Pripojí potomka k uzlu
    def add_child(self, child):
        self.children.append(child)

    # Magická funkcia, ktorá umožní výpis stromu volaním funkcie print()
    def __str__(self):
        return f'\nNode {self.data} with children: {self.children}'

    __repr__ = __str__


# Strom z obrázku vyššie je možné skonštruovať takto:
g_subtree = Node('G')
g_subtree.add_child(Node('H'))
g_subtree.add_child(Node('I'))

c_subtree = Node('C')
c_subtree.add_child(g_subtree)

b_subtree = Node('B')
b_subtree.add_child(Node('D'))
b_subtree.add_child(Node('E'))
b_subtree.add_child(Node('F'))

# Vytvorenie koreňa stromu
tree = Node('A')
tree.add_child(b_subtree)
tree.add_child(c_subtree)

# Vypíše strom
print(tree)
# Node A with children: [
# Node B with children: [
# Node D with children: [],
# Node E with children: [],
# Node F with children: []],
# Node C with children: [
# Node G with children: [
# Node H with children: [],
# Node I with children: []]]]