class Tree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def insert(self, value):
        def put(current, value):
            if current is None:
                node = Tree(value)
                node.parent = self
                return node
            else:
                current.insert(value)
                return current

        if value > self.value:
            self.right = put(self.right, value)
        else:
            self.left = put(self.left, value)

    def find(self, pred):
        def do(node):
            if node is None:
                return None
            elif pred(node):
                return node
            else:
                return do(node.left) or do(node.right)
        return do(self)

    def findByValue(self, value):
        return self.find(lambda node: node.value == value)

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
                    if parent is not None:
                        if (index % 2) == 0:
                            parent.left = node
                        else:
                            parent.right = node
                        node.parent = parent
                else:
                    head = node
                current_level.append(node)
            previous_level = current_level
        return head

