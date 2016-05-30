# remove duplicates from unsorted linked list
from Node import Node

# method for removing duplicates from linked list
def remove_duplicates(n):
    start = n
    lst = Node(n.value)
    visited = [n.value]
    while start.next:
        if start.value in visited:
            start = start.next
        else:
            visited.append(start.value)
            lst.add_to_tail(start.value)
            start = start.next

    return lst

# method for removing duplicate from linked list withoud additional buffer
def remove_duplicates_without_additional_space(n):
    start = n
    while start:
        v = start.value
        end = start.next
        while end and end.next:
            tmp = end.next
            found = False
            while tmp and tmp.value == v:
                tmp = tmp.next
                found = True
            if found:
                # if tmp and tmp.next:
                if tmp:
                    end.next = tmp.next
                else:
                    end = None
            else:
                end = end.next
        start = start.next
    return n

n = Node(1)
n.add_to_tail(1)
n.add_to_tail(1)
n.add_to_tail(1)
n.add_to_tail(1)
n.add_to_tail(1)

n = remove_duplicates_without_additional_space(n)

n.print_items()
