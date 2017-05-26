class Tree:
    def __init__(s, value):
        s.value = value
        s.left = None
        s.right = None

    def insert(self, value):
        def put(current, value):
            if current is None:
                return Tree(value)
            else:
                current.insert(value)
                return current

        if value > self.value:
            self.right = put(self.right, value)
        else:
            self.left = put(self.left, value)

    def to_tuple(self):
        def fill(node):
            if node is not None:
                if (node.left is None) and (node.right is None):
                    return node.value
                else:
                    return (node.value, fill(node.left), fill(node.right))
            else:
                return None
        return fill(self)

    @staticmethod
    def create_normal(values):
        head = None
        for value in values:
            if head is None:
                head = Tree(value)
            else:
                head.insert(value)
        return head

    @staticmethod
    def create_like(levels):
        head = None
        previous_level = []
        for (depth, level) in enumerate(levels):
            current_level = []
            for (index, value) in enumerate(level):
                node = None if value is None else Tree(value)
                if depth > 0:
                    parent = previous_level[int(index / 2)]
                    if (index % 2) == 0:
                        parent.left = node
                    else:
                        parent.right = node
                else:
                    head = node
                current_level.append(node)
            previous_level = current_level
        return head

