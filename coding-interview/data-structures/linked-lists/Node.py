

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def add_to_tail(self,  value):
        d = Node(value)
        n = self
        while n.next != None:
            n = n.next
        n.next = d

    def add_to_top(self, value):
        d = Node(value)
        d.next = self
        return d

    def print_items(self):
        item = self
        while item:
            print(item.value)
            item = item.next

    def del_by_key(self, obj, key):
        if key == 0:
            return obj.next
        else:
            obj.next = self.del_by_key(obj.next, key - 1)
        return obj

