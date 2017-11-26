from collections import deque

def answer(start, end):
    """
    Inputs:
        start (Node): the starting node
        end (Node):
    Returns:
        path_exists (Boolean): True if there is a path
    """

    # using breadth first search
    node = start
    queue = deque([])

    path_exists = False

    if node == end:
        path_exists = True

    else:
        # use breadth first search
        while node.nxt != []:

            for element in node.nxt:
                queue.append(element)

            node = queue.popleft()
            if node == end:
                path_exists = True
                break

    return path_exists


# implementing a Node class just for shits
class Node:
    """
        Classes that implements a node for a directional graph
    """

    def __init__(self, value):
        self.value = value
        self.nxt = []
        self.visited = False

    def add(self, element):
        nxt.append(element)

    def reset_visited(self):
        self.visited = False

def main():

main()
