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

    @staticmethod
    def create(values):
        head = None
        for value in values:
            if head is None:
                head = Tree(value)
            else:
                head.insert(value)
        return head

