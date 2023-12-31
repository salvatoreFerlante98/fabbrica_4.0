class Node:
    def __init__(self, value):
        self.value = value
        self.children = []
        self.parent = None

    def __add__(self, other):
        self.children.append(Node(other))

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
        elif not node.children:
            return None
        else:
            for child in node.children:
                result = self._recursive_get_child(child, value)
                if result:
                    return result
            return None

    def __str__(self):
        return str(self.value)


class TreeMultiLeaf:
    def __init__(self, root):
        self.root = Node(root)

    def __add__(self, other):
        self.root.add_child(Node(other))

    def __sub__(self, other):
        self.root.remove_child(Node(other))

    def __getitem__(self, item):
        return self.root.get_child(item)

    def add_subchild(self, parent, child):
        self[parent] + child

    def remove_subchild(self, child):
        self.root.get_child(child).remove_child(Node(child))
