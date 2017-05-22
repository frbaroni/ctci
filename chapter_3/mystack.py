class Stack:
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        return self.data.pop()

    def peek(self):
        if len(self.data) > 0:
            return self.data[-1:][0]
        else:
            return None
