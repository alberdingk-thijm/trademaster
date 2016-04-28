"""
Implementation of Dijkstra's algorithm to find
all shortest paths from a given source to the other
vertices of the graph.

The graph is a dictionary of {vertex: list of (neighbour vertex, edge weight)}.
"""

from fib_heap import *

class NamedFibHeap(FibonacciHeap):
    def insert(self, data, name):
        n = self.NamedNode(data, name)
        n.left = n.right = n
        self.merge_with_root_list(n)
        if self.min_node is None or n.data < self.min_node.data:
            self.min_node = n
        self.total_nodes += 1
        return n

    def get_names(self):
        head = self.find_min()
        if head is None:
            return []
        else:
            return [x.name for x in self.iterate(head)]

def dijkstra(G, s):
    """
    Return a tuple of dictionaries of ({v: sum weight from s to v},{v: path from s to v}),
    determined using Dijkstra's algorithm.
    Inputs:
    - G, a weighted undirected graph
    - s, a source vertex in the graph G
    """

    D = {} # distances
    P = {} # predecessors
    N = {} # nodes
    Q = NamedFibHeap()

    for v in G.keys():
        D[v] = float('inf')
        P[v] = None
        if v != s:
            N[v] = Q.insert(D[v], v)
    D[s] = 0

    N[s] = Q.insert(D[s], s)

    while Q.total_nodes > 0:
        u = Q.extract_min()
        for (nbr, w) in G[u.name]:
            alt = D[u.name] + w
            if alt < D[nbr]: # if new dist shorter
                D[nbr] = alt
                P[nbr] = u.name
                Q.decrease_key(N[nbr], alt)

    return (D, P)

if __name__ == "__main__":
    G = {'a': [('b', 2), ('c', 3)], 'b': [('a', 2)], 'c': [('a', 3)]}
    print dijkstra(G, 'a')
