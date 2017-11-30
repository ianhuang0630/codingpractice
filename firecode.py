def fib(n):
	coll = {}
	return fib_rec(n, coll)

def fib_rec(n, coll):

	if n <= 1:
		return n
	
	else:
		if (n-1) not in coll:
			coll[n-1] = fib_rec(n-1, coll)
		if (n-2) not in coll:
			coll[n-2] = fib_rec(n-2, coll)

		return coll[n-1] + coll[n-2]

class BinaryTree:
	def __init__(self, root_node = None):
		self.root = root_node

	def number_of_leaves(self):
		if self.root == None:
			return 0

		elif self.root.left_child == None and self.root.right_child == None:
			return 1

		bt_left = BinaryTree(self.root.left_child)
		bt_right = BinaryTree(self.root.right_child)

		return bt_left.number_of_leaves() + bt_right.number_of_leaves()

class TreeNode:
	def __init__(self, data, left_child = None, right_child = None):
		self.data = data
		self.left_child = left_child
		self.right_child = right_child

def insert_star_between_pairs(a_string):
	"""
	An iterative approach for O(n) time 
	"""

	prev = ""

	dup_list = []

	for (idx,character) in enumerate(a_string):
		if character == prev:
			dup_list.append(idx)
		else:
			prev = character


	dup_list = [element + idx for (idx, element) in enumerate(dup_list)]


class SinglyLinkedList:
    #constructor
    def __init__(self):
        self.head = None
        
    #method for setting the head of the Linked List
    def setHead(self,head):
        self.head = head
                      
    #method for inserting a new node at the end of a Linked List   
    def insertAtEnd(self,data):
        new_node = Node()
        new_node.setData(data)

        if self.head != None:
            node = self.head
            while node.getNext() != None:
                node = node.getNext()
               
    
            node.setNext(new_node)
            
        else:
            self.setHead(Node().setData(data))

    def __str__(self):
    	result = []
    	node = self.head
    	while node!=None:
    		result.append(node.data)
    		node = node.next

    	return str(result)


class Node:
    def __init__(self):
        self.data = None
        self.next = None
     
    def setData(self,data):
        self.data = data
      
    def getData(self):
        return self.data
     
    def setNext(self,next):
        self.next = next
     
    def getNext(self):
        return self.next



A = Node()
A.setData(3)
B = Node()
B.setData(2)
C = Node()
C.setData(1)
A.next = B
B.next = C


l = SinglyLinkedList()
l.setHead(A)
l.insertAtEnd(4)
print(l)
