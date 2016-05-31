

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

    def remove_duplicates(self):
        start = self
        lst = Node(self.value)
        visited = [self.value]
        while start:
            if start.value not in visited:
                lst.add_to_tail(start.value)
                visited.append(start.value)

            start = start.next
        return lst

    def remove_duplicates_without_additional_space(self):
        start = self
        while start:
            v = start.value
            end = start
            while end and end.next:
                while end.next and end.next.value == v:
                    end.next = end.next.next
                end = end.next
            start = start.next

    def find_nth_last_element(self, n):
        start = self
        end = self
        c = 0
        while end:
            c += 1
            end = end.next
        t = c - n
        while start and t:
            t -= 1
            start = start.next

        if start and t == 0:
            return start.value
        else:
            return -1

    def remove_middle_element(self):
        c = 0
        start = self
        end = self
        while end.next:
            c += 1
            end = end.next
        m = c // 2

        while start and m > 1:
            start = start.next
            m -= 1

        start.next = start.next.next

    def add_linked_lists(self, lst: list):
        pass