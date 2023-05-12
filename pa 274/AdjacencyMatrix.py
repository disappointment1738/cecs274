from Interfaces import Graph, List
import ArrayList
import ArrayQueue
import ArrayStack
import numpy as np
"""An implementation of the adjacency list representation of a graph"""

class AdjacencyMatrix(Graph):

    def __init__(self, n : int):
        self.n = n
        self.adj = np.zeros((self.n, self.n), dtype=int)

    def add_edge(self, i : int, j : int):
        # todo
        # add the edge (i, j) to E
        #pre-condition
        # if 0 < i or i >= self.n or j < 0 or j >= self.n:
        # if i >= self.n or j >= self.n:
        #     return False
        # self.adj[i][j] = True
        if 0 <= i and j < self.n:
            self.adj[i][j] = True
        return False



    def remove_edge(self, i : int, j : int):
        # precondition
        if 0 <= i and j < self.n:
            if self.adj[i][j]:
                self.adj[i][j] = False
                return True
        return False

    def has_edge(self, i : int, j: int) ->bool:
        # precondition
        if i >= self.n or j >= self.n:
            return False
        return self.adj[i][j]

    def out_edges(self, i) -> List:
        """returns a list of all integers j such that (i,j) is in E"""
        edges = []
        for j in range(0, self.n):
            if self.adj[i][j] == True:
                edges.append(j)
        return edges

    def in_edges(self, j) -> List:
        """returns a list of all integers i such that (i, j) is in E"""
        edges = []
        for i in range(0, self.n):
            if self.adj[i][j] == True:
                edges.append(i)
        return edges


    def bfs(self, r : int):
        # initialize
        traversal = []
        seen = [False] * self.n
        q = ArrayQueue.ArrayQueue()
        # visit vertix r
        q.add(r)
        traversal.append(r)
        seen[r] = True

        while q.size() != 0:
            current = q.remove()
            neighbors = self.out_edges(current)
            for i in neighbors:
                if seen[i] is False:
                    q.add(i)
                    traversal.append(i)
                    seen[i] = True
        return traversal


    def dfs(self, r : int):
        # initialize
        traversal = []
        s = ArrayStack.ArrayStack()
        seen = [False] * self.n
        # push r into stack
        s.push(r)
        while s.size() != 0:
            current = s.pop()
            if seen[current] is False:
                traversal.append(current)
                seen[current] = True
            neighbors = self.out_edges(current)
            neighbors.reverse()
            for i in neighbors:
                if seen[i] is False:
                    s.push(i)
        return traversal

    def size(self):
        return self.n

    def __str__(self):
        s = ""
        for i in range(0, self.n):
            s += "%i:  %r\n" % (i, self.adj[i].__str__())
        return s

