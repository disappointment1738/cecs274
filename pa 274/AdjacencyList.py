"""An implementation of the adjacency list representation of a graph"""
from Interfaces import Graph, List
import numpy as np
import copy
import ArrayList
import ArrayStack
import ArrayQueue


class AdjacencyList(Graph):
    def __init__(self, n : int):
        self.n = n
        self.adj = np.zeros(n, dtype=ArrayList.ArrayList)
        for i in range(self.n):
            self.adj[i] = ArrayList.ArrayList()

    def add_edge(self, i : int, j : int):
        # todo
        # add the edge (i, j) to E
        if 0 <= i and j < self.n:
            for k in range(len(self.adj[i])):
                if self.adj[i].get(k) == j:
                    return False
            self.adj[i].append(j)
            return True
        # return False
        # if i >= self.n or j >= self.n:
        #     return False
        # self.adj[i].append(j)

    def remove_edge(self, i : int, j : int):
        # todo
        # remove the edge (i,j) from E
        # if i >= self.n or j >= self.n:
        #     return False
        if 0 <= i and j < self.n:
            for k in range(len(self.adj[i])):
                if self.adj[i].get(k) == j:
                    self.adj[i].remove(k)
                    return True
        return False

    def has_edge(self, i : int, j: int) ->bool:
        # todo
        # returns true if the edge (i,j) exists in E
        # if i >= self.n or j >= self.n:
        #     return False
        if 0 <= i and j < self.n:
            for k in range(len(self.adj[i])):
                if self.adj[i].get(k) == j:
                    return True
        return False

    def out_edges(self, i) -> List:
        # todo
        # returns a list of all integers j such that (i,j) in E
        return self.adj[i]

    def in_edges(self, j) -> List:
        # todo
        if j > self.n:
            return False
        incoming = []
        for k in range(self.n):
            if self.has_edge(k,j):
                incoming.append(k)
        return incoming



    def bfs(self, r : int):
        # todo
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
        # todo
        # initialize
        traversal = []
        s = ArrayStack.ArrayStack()
        seen = [False] * self.n
        # push r into stack
        s.push(r)
        # start_index = r
        while s.size() != 0:
            current = s.pop()
            if seen[current] is False:
                traversal.append(current)
                seen[current] = True
            neighbors = self.out_edges(current)
            # neighbors.reverse()
            for i in reversed(neighbors):
                if seen[i] is False:
                    s.push(i)
            # start_index += 1
        return traversal

    def size(self):
        return self.n

    def __str__(self):
        s = ""
        for i in range(0, self.n):
            s += "%i:  %r\n" % (i, self.adj[i].__str__())
        return s

    def __str__(self):
        s = ""
        for i in range(0, self.n):
            s += "%i,%r\n" % (i, self.adj[i].__str__())
        return s

# test = AdjacencyList(3)
# print(test.add_edge(3,3))

# test.
# test.add_edge(4,3)