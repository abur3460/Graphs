"""
Simple graph implementation
"""
from collections import deque
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id] if vertex_id in self.vertices else set()

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        stack = deque()  # init double ended stack
        discovered = set()  # init discovered node set
        stack.append(starting_vertex)  # add starting
        while len(stack) > 0:
            currNode = stack.popleft()
            if currNode not in discovered:
                discovered.add(currNode)
                print(currNode)
                for neighbor in self.get_neighbors(currNode):
                    stack.append(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stack = deque()  # init double ended queue
        discovered = set()  # init discovered node set
        stack.append(starting_vertex)  # add starting
        while len(stack) > 0:
            currNode = stack.pop()
            if currNode not in discovered:
                discovered.add(currNode)
                print(currNode)
                for neighbor in self.get_neighbors(currNode):
                    stack.append(neighbor)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        discovered = set()

        def dft(vertex):
            if vertex in discovered:
                return
            else:
                discovered.add(vertex)
                print(vertex)

            neighbors = self.get_neighbors(vertex)

            for neighbor in neighbors:
                dft(neighbor)

        dft(starting_vertex)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # create empty queue and enque path to starting vertex
        queue = Queue()
        queue.enqueue([starting_vertex])
        # create an empty set to track discovered vertices
        visited = set()
        # while the queue is not empty
        while queue.size() > 0:
            currrent_path = queue.dequeue()
            print(f'\nthe currrent_path is {currrent_path}')
            current_node = currrent_path[- 1]
            print(f'\nthe current_node is {current_node}')
            if current_node == destination_vertex:
                return currrent_path
            if current_node not in visited:
                visited.add(current_node)
                print(f'visted: {visited}')
                for neighbor in self.get_neighbors(current_node):
                    newPath = list(currrent_path)
                    newPath.append(neighbor)
                    print(f'the new path is: {newPath}')
                    queue.enqueue(newPath)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = deque()  # init double ended queue
        # each element in the stack is the current path e.g [1, 2, 3...]
        stack.append([starting_vertex])
        discovered = set()
        while len(stack) > 0:
            currPath = stack.pop()  # [1, 2, 3]
            currNode = currPath[-1]  # 3
            if currNode == destination_vertex:
                return currPath
            if currNode not in discovered:
                discovered.add(currNode)
                for neighbor in self.get_neighbors(currNode):
                    newPath = list(currPath)
                    newPath.append(neighbor)
                    stack.append(newPath)
                    print(stack)

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        This should be done using recursion.
        """
        discovered = set()

        def dfs(path):
            last_vertex = path[-1]

            if last_vertex in discovered:
                return None

            else:
                discovered.add(last_vertex)

            if last_vertex == destination_vertex:
                return path

            for neighbor in self.get_neighbors(last_vertex):
                next_path = path[:]
                next_path.append(neighbor)

                found = dfs(next_path)

                if found:
                    return found

            return None

        return dfs([starting_vertex])


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
