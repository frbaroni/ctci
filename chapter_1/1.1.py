def uniqueChars(string):
    def already_on_set(char, storage):
        if char in storage:
            return True
        storage.add(char)
        return False
    storage = set()
    return not any(already_on_set(char, storage) for char in string)

def test(text):
    print('{0} = {1}'.format(text, uniqueChars(text)))
    

test(input())
