
class LinkedList(object):
    def __init__(self, v = None, next = None):
        self.value = v
        self.next = next


class Stack(object):
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, value):
        self.size += 1
        nhead = LinkedList(value)
        nhead.next = self.head
        self.head = nhead
    
    def pop(self):
        nhead = self.head
        c = 0
        while nhead.next != None and c < self.size:
            nhead = nhead.next
            c += 1
        print(nhead.value)
        self.size -= 1

        




while True:
    command, value = input().split()
    print(command)
    print(value)


    




