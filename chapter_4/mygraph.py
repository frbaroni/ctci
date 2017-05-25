class GraphNode:
    def __init__(self, name):
        self.children = []
        self.name = name

    def connect(self, node):
        self.children.append(node)

    @staticmethod
    def create(elements, bidirectional=True):
        nodes = {}
        for e in elements:
            (a, b) = e.split(' -> ')
            nodes[a] = nodes.get(a, GraphNode(a))
            nodes[b] = nodes.get(b, GraphNode(b))
            na = nodes[a]
            nb = nodes[b]
            na.connect(nb)
            if bidirectional:
                nb.connect(na)
        return nodes

    def __str__(self):
        return 'GraphNode({})'.format(self.name)

