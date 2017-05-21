class LinkedList:
    def __init__(s, value):
        s.data = value
        s.next = None

    def toList(self):
        res = []
        n = self
        while n is not None:
            res.append(n.data)
            n = n.next
        return res

    @staticmethod
    def create(elements):
        res = None
        for element in reversed(elements):
            e = LinkedList(element)
            if res is not None:
                e.next = res
            res = e
        return res
