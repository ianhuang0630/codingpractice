from collections import deque

# Graphs practice
MAX = 600000

class EdgeNode:
    def __init__(self, y):
        self.y = y
        self.weight = None
        self.next = None


# TODO: change the edges and degree variables to become dictionaries instead of lists

class Graph:
    def __init__(self, directed):
        """
        Inputs:
            directed (bool): True if graph is directed
        """

        self.nvertices = 0
        self.nedges = 0
        self.directed = directed

        self.degree = [0] * MAX
        self.edges = [None] * MAX

        self.vertice_labels = set([])


    def add_edge(self, x, y, directed=None):
        """
        Inputs:
            x (int): start
            y (int): end
        """

        if directed == None:
            directed = self.directed

        if x not in self.vertice_labels:
            self.vertice_labels.add(x)
            self.nvertices = len(self.vertice_labels)


        # create EdgeNode object, placed at edges[x], holding y
        if self.edges[x] == None:
            self.edges[x] = EdgeNode(y)
            self.degree[x] += 1
        else: # assumption that inputs would not duplicate a preexisting edge

            # instead of traversing the linked list, just insert at the beginning
            # this would switch the order, the last node connected is seen as
            # the first node.
            current_chain = self.edges[x]
            self.edges[x] = EdgeNode(y)
            self.edges[x].next = current_chain

            # self.edges[x].next = EdgeNode(y)
            self.degree[x] += 1

        if not directed:
            self.add_edge(y,x,directed=True)
        else:
            self.nedges += 1

    def print_graph(self):
        # printing edges - this is assuming that vertices are denoted starting
        # from 0
        for i in range(self.nvertices):
            # print all pairs
            n = self.edges[i]
            while n != None:
                print("{} to {}".format(i,n.y))
                n = n.next

            print("") # prints new line

def bfs(graph, start, f_vertex, f_edge, f_vertex_late):
    """
    Input:
        grpah (Graph): the graph traversed
        start (int): the starting node.
        f_vertex (func): operation that one would like to perform on every vertex.
        f_edge (func): oepration performed on every edge.
        f_vertex_late (func): operation performed after the neighborhood is visited.

    Returns:
        parents (list): containing the label of the parent of the ith node
            in the ith position in the list.
    """

    visited = [False]*graph.nvertices #FIXME:only works when not directed
    processed = [False]*graph.nvertices
    parents = [-1] * graph.nvertices

    q = deque()
    q.append(start)
    current_node = start

    visited[current_node] = True

    while len(q) != 0:
        # enqueue all nodes connected to start

        # pop the queue and then process the first thing in the queue
        current_node = q.popleft()

        # TODO: process node
        f_vertex(current_node)
        processed[current_node] = True

        conn_edgeNode = graph.edges[current_node]

        # find the next node linked to current_node until no more
        while conn_edgeNode != None:
            conn_node = conn_edgeNode.y

            if not visited[conn_node]: # if not visited
                q.append(conn_node) # appending the next value
                visited[conn_node] = True
                parents[conn_node] = current_node

            if not processed[conn_node] or graph.directed: #XXX: still don't really understand
                f_edge(current_node, conn_node)

            conn_edgeNode = conn_edgeNode.next

        f_vertex_late(current_node) # a function that processes the vertex
        # after its neighborhood is visited (instead of processed)

    return (parents, visited)

def dfs_stack(graph, start, f_vertex, f_edge, f_vertex_late):
    """
    Input:
        graph (Graph): the graph traversed
        start (int): the starting node.
        f_vertex (func): operation that one would like to perform on every vertex.
        f_edge (func): oepration performed on every edge.
        f_vertex_late (func): operation performed after the neighborhood is visited.

    Returns:

    """

    visited = [False] * graph.nvertices
    processed = [False] * graph.nvertices

    visited[start] = True
    s = []
    s.append(start)

    current_node = start

    while len(s) != 0:

        # pop from stack and process first node
        current_node = s.pop()
        f_vertex(current_node)
        processed[current_node] = True

        conn_EdgeNode = graph.edges[current_node]

        # for all connected nodes to this node, find the
        while conn_EdgeNode != None:
            conn_node = conn_EdgeNode.y
            if not visited[conn_node]:
                s.append(conn_node)
                visited [conn_node] = True

            # if conn_node has not been processed,
            if not processed[conn_node] or graph.directed:
                f_edge(current_node, conn_node) # TODO; fix placement

            conn_EdgeNode = conn_EdgeNode.next

        f_vertex_late(current_node)

def dfs_recursive(graph, start, f_vertex, f_edge, f_vertex_late, visited = None):
    """
    Input:
        graph (Graph): the graph traversed
        start (int): the starting node.
        f_vertex (func): operation that one would like to perform on every vertex.
        f_edge (func): oepration performed on every edge.
        f_vertex_late (func): operation performed after the neighborhood is visited.

    Returns:
    """

    # base case: start is not connected to any nodes -- graph.edges[start].next == None

    if visited == None:
        visited = [False] * graph.nvertices

    if start == None:
        return ([-1]*graph.nvertices, [False]*graph.nvertices)

    # if graph.edges[start] == None:
    #     return ([-1]*graph.nvertices, [False]*graph.nvertices)
    # elif visited[graph.edges[start].y]:
    #     return ([-1]*graph.nvertices, [False]*graph.nvertices)

    # for every node that the current_node is linked to, do a recursive call
    else:
        # operation on node

        processed = [False] * graph.nvertices
        parents = [-1] * graph.nvertices

        f_vertex(start)
        visited[start] = True
        processed[start] = True

        next_EdgeNode = graph.edges[start]

        # compile all connected nodes
        while next_EdgeNode != None:
            conn_node = next_EdgeNode.y

            if not visited[conn_node]:
                parents[conn_node] = start
                visited[conn_node] = True

                (parents_new, visited_new) = dfs_recursive(graph, conn_node, f_vertex, f_edge, f_vertex_late, visited)

                # combine visited and parents
                visited = [visited[i] or visited_new[i] for i in range(len(visited))]
                parents = [max(parents[i], parents_new[i]) for i in range(len(parents))]

            if not processed[conn_node] or graph.directed:
                f_edge(start, conn_node)

            next_EdgeNode = next_EdgeNode.next

        f_vertex_late(start) # after every single neighbor is visited

        return visited, parents


class ConnectedVerifier:

    def __init__(self):
        pass

    def verify_connected(self, graph):
        """
        Input:
            graph (Graph): the graph being verified
        Output:
            counter (int): The number of components in the graph

        """

        edges = graph.edges
        vertices = graph.vertice_labels
        visited = [False] * graph.nvertices

        # using breadth-first traversal, and if reaches end of traversal but
        # not all edges are visited, then connected = False

        def f_vertex(v):
            print ("vertex: {}".format(v))

        def f_edge(i,v):
            print ("edge: {} to {}".format(i, v))

        def f_vertex_late(v):
            pass

        counter = 0

        while not all(visited):
            # find the first unvisited O(n)
            counter += 1
            start = visited.index(False)
            # bfs (O(n))

            print ("Component {}".format(counter))
            newly_visited = bfs(graph,start, f_vertex, f_edge, f_vertex_late)[1]

            # merging O(n)
            visited = [visited[i] or newly_visited[i] for i in range(len(newly_visited))]

        return counter

class TwoColor:
    def __init__(self, graph):
        self.graph = graph
        self.color = ["uncolored"] * graph.nvertices
        self.bipartite = True

    def verify_bipartite(self):
        """
        Inputs:
            graph (Graph): input graph being verified
        Outputs:
            bipartite (bool): True if graph is bipartite
        """

        # traverse through the graph. every child is given the opposite
        # color as its parent.

        def f_vertex(v):
            # TODO: assign colors
            pass
            # if self.color[v] == "uncolored":
            #     if self.parent[v] != -1: # if not the root
            #         self.color[v] = self.opposite(self.color[parent[v]])
            #
            #     else: # assinging the origin "white"
            #         self.color[v] = "white"
            # else:
            #     print ("node {} traversed again".format(v))

        def f_edge (i, v):
            # TODO: match colors, if doesn't match, then print doesn't match

            if self.color[i] == self.color[v]:
                self.bipartite = False
            else:
                self.color[v] = self.opposite(self.color[i])

        def f_vertex_late(v):
            pass

        # while some still uncolored

        while any ([element == "uncolored" for element in self.color]):
            # find the first that is uncolored
            start = self.color.index("uncolored")
            self.color[start] = "white"

            bfs(self.graph, start, f_vertex, f_edge, f_vertex_late)

            # merging update_parents with parents O(n)
        return self.bipartite

    def opposite (self, color):
        """
        Inputs:
            color: String of input color
        Outputs:
            complement: String of output color
        """
        if color == "white":
            return "black"
        elif color == "black":
            return "white"
        else:
            return "uncolored"


class TreeNode:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)

class BinarySearchTree:
    def __init__ (self, root=None):
        self.root = root

    def build(self,m):
        """
        Inputs:
            m (list): a sorted list of elements
        Returns:
            self.root (TreeNode): root of the binary search tree.
        """

        if not m:
            return None
        if len(m) == 1:
            return TreeNode(m[0])
        # construct at the center
        center = len(m)//2

        node = TreeNode(m[center])
        node.right = self.build(m[center+1:])
        node.left = self.build(m[:center])

        self.root = node

        return self.root

    def bst_sequences(self):

        def all_possible(kids):
            """
            returns list of lists of different permutations of the kids elements
            e.g. [[1,2], [2,1]]
            """
            if len(kids) == 1:
                return [kids]
            else:
                b = []
                for i in range(len(kids)):
                    for_i = all_possible(kids[:i] + kids[i+1:])
                    b.extend([[kids[i]] + element for element in for_i])
                return b

        def combine_kids(gens):
            """
            Inputs:
                gens (list of lists):
                    [[3],[1,5],[0,2,4,6]]
            returns list of lists of different permutations
            """
            # gens[0] combine with combine_kids(gens[1:])

            if len(gens) == 1:
                return all_possible(gens)
            else:
                header = gens[0]
                # combining the header and every element of all_possible()]
                
        d = deque()
        d.add(self.root)

        total = [] # is list of lists of children of same generation

        while d:
            x = []
            while d:
                x.append(d.popleft())
            total.append(x)
            for i in x:
                q.add(i.left)
                q.add(i.right)

        # operations on total


    def __str__(self):
        # doing a in_order traversal
        if self.root == None:
            tree = ""
        else:
            bst_left = BinarySearchTree(root = self.root.left)
            bst_right = BinarySearchTree(root = self.root.right)
            tree = str(bst_left) + str(self.root) + str(bst_right)

        return tree

def main():
    def f_vertex(v):
        print ("vertex: {}".format(v))

    def f_edge(i,v):
        print ("edge: {} to {}".format(i, v))

    def f_vertex_late(v):
        pass

    g = Graph(False)
    g.add_edge(0,1)
    g.add_edge(0,2)
    g.add_edge(1,5)
    g.add_edge(1,6)
    g.add_edge(2,3)
    g.add_edge(2,4)
    # g.add_edge(5,6)

    #     0
    #   1   2
    # 5 6  3 4

    print ("Enumerating elements of graph: \n")

    [print("{}'s parent is {}".format(idx, element )) for (idx, element)
        in enumerate(bfs(g, 0, f_vertex, f_edge, f_vertex_late)[0])]
    print ("")

    cv = ConnectedVerifier()
    print ("Checking if connected: \n")
    print ("There are {} component(s).".format(cv.verify_connected(g)))
    print ("")

    # tc = TwoColor(g)
    # print ("checking if bipartite: \n")
    # print ("The graph is{} bipartite".format("" if tc.verify_bipartite() else " not"))
    #
    # print ("Enumerating elements of graph through dfs_stack \n")
    # dfs_stack(g, 0, f_vertex, f_edge, f_vertex_late)
    #
    # print ("Enumerating elements of graph through dfs_recursive \n")
    # dfs_recursive(g, 0, f_vertex, f_edge, f_vertex_late)

    bst = BinarySearchTree()
    m = [1,2,3,4,5,6,7,8,9]
    bst.build(m)

    print(bst)


if __name__ == "__main__":
    main()
