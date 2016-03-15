
class Node(object): 
    def __init__(self, data=None, next_node=None, prev_node = None):
        self.data = data
        self.next = next_node
        self.prev = prev_node
	
def InsertTop(head, data):
    n = Node(data)
    if head == None:
        return n
    else:
        rest = InsertTop(head.next, data)
        rest.next = head
        head = rest
        return head

"""
INSERT INTO END OF DOUBLY LINKED LIST
"""
def InsertBottom(head, data):
    n = Node(data)
    if head == None:
        return n
    else:
        rest = InsertBottom(head.next, data)
        head.next = rest
        rest.prev = head
        return head

"""
INSERT INTO SORTED POSITION OF DOUBLY LINKED LIST
"""
def SortedInsert(head, data):
    n = Node(data)
    if head == None:
        return n
    else:        
        if data <= head.data:
            n.next = head
            head.prev = n
            return n
        else:
            rest = SortedInsert(head.next, data)
            head.next = rest
            rest.prev = head
            return head
    
"""
REVERSE LINKED LIST
"""
def Reverse(head):
    next_node = head.next
    pcurrent = head
    phead = None
    if pcurrent:
        while pcurrent != None:
            next_node = pcurrent.next
            pcurrent.next = phead
            pcurrent.prev = next_node
            phead  = pcurrent
            pcurrent = next_node
        return phead        
    else:
        return None



def ReversePrint(head):
    next_node = head.next
    pcurrent = head
    phead = None
    if pcurrent:
        while pcurrent.next != None:
            pcurrent = pcurrent.next

        while pcurrent != None:
            print(pcurrent.data)
            pcurrent = pcurrent.prev
    else:
        return None    

def DeleteNode(head, data):
    if head.data == data:
        head = head.next
        return head
    else:
        head.next = DeleteNode(head.next, data)
        return head

head = None	        
head = InsertBottom(head, 1)
head = InsertBottom(head, 2)
head = InsertBottom(head, 4)
head = InsertBottom(head, 4)
head = InsertBottom(head, 3)

ReversePrint(head)