class Node(object): 
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


def InsertBottom(head, data):
	n = Node(data)
	if head == None:
		return n        
	else:
		head.next = InsertBottom(head.next, data)
		return head

def InsertTop(head, data):
	n = Node(data)
	if head == None:
		return n
	else:
		n.next = head
		return n




def printNodes(head):
	while head != None:
		print(head.data)
		head = head.next

def Reverse(head):
    next_node = head.next
    pcurrent = head
    phead = None
    if pcurrent:
	  	while pcurrent != None:
	  		nextHead = pcurrent.next
			pcurrent.next = phead
			phead = pcurrent
			pcurrent = nextHead
		return phead	

def InsertAtPosition(head, data, position):
	if position == 0 or head == None:
		n = Node(data)
		n.next = head
		return n
	else:
		head.next = InsertAtPosition(head.next, data, position - 1)
		return head

head = None
head = InsertBottom(head, 1)		
head = InsertBottom(head, 2)		
head = InsertBottom(head, 3)		
head = InsertBottom(head, 5)
head = InsertAtPosition(head, -1, 1)		
printNodes(head)