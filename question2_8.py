def answer(node):

    """
    Input:
        node (Node): the starting node of a list
    Output
        circular (boolean): True if list is circular
    """

    # putting all nodes.data in a dictionary, a hash map
    dic = {}

    current_node = node
    circular = False

    while True:
        # traversing the list and adding node to the dictionary

        if current_node.data in dic:
            circular = True
            break
        else:
            dic[current_node.data] = 1 # arbitrary value

        if current_node.next == None:
            break
        else:
            current_node = current_node.next

    return circular

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def append(self, data):
        new_node= Node(data)
        self.next = new_node

    def add_end(self, data):
        new_node = Node(data)
        current_node = self
        while current_node.next != None:
            current_node = current_node.next

        current_node.next = new_node

    def print_as_string(self):
        node = self
        print (node.data)
        while node.next != None:
            node = node.next
            print (node.data)


def main():

    node = Node(1)
    node.add_end(2)
    node.add_end(3)
    node.add_end(1)

    node.print_as_string()
    print(answer(node))

main()
