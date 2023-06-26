class Node:
    def __init__(self, value):
        self.value = value
        self.children = []
        self.parent = None

    def add_child(self, child_node):
        self.children.append(child_node)
        child_node.parent = self

    def remove_child(self, child_node):
        self.children = [child for child in self.children if child != child_node]
        child_node.parent = None

    def get_parent(self):
        return self.parent

    def get_child(self, value):
        return self._recursive_get_child(self, value)

    def _recursive_get_child(self, node, value):
        if node.value == value:
            return node
        else:
            for child in node.children:
                return self._recursive_get_child(child, value)

    def __str__(self):
        return str(self.value)


class Tree:
    def __init__(self, root):
        self.root = Node(root)

    def __add__(self, other):
        self.root.add_child(Node(other))

    def __sub__(self, other):
        self.root.remove_child(Node(other))

    def addSubchild(self, parent, child):
        parent.add_child(Node(child))

    def removeSubchild(self, child):
        self.root.get_child(child).remove_child(Node(child))

    def search(self, value):
        return "" + self.root.get_child(value)