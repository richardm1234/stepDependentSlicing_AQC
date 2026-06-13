import sys
import math
import random
from itertools import combinations

def contract(G, v):
    """
    Contract in-place a tensor index by removing a node and turning its neighbors into a clique

    Args:
         G (nx.Graph): graph
         v (int): the node to be removed

    Returns:
          nx.Graph: graph G after contracting node v
    """
    neighbors = list(G.neighbors(v))
    G.add_edges_from(combinations(neighbors, 2))
    G.remove_node(v)
    return G

def greedy(G):
    """
    Implementation of the greedy algorithm

    Args:
        G (nx.Graph): graph

    Returns:
        list[int], list[int], int: the ordering, the width profile and the contraction width
    """
    G_copy = G.copy()
    order = []
    width = 0
    widthProfile = []

    while G_copy.number_of_nodes() > 0:

        minDeg = sorted(G_copy.nodes(), key=lambda v: G_copy.degree(v))[0]
        widthProfile.append(G_copy.degree(minDeg))
        width = max(width, G_copy.degree(minDeg))
        order.append(minDeg)

        contract(G_copy, minDeg)

    return order, widthProfile, width

def rgreedy(G, tau, q):
    """
    Implementation of the randomized greedy ordering algorithm

    Args:
        G (nx.Graph): graph
        tau (float): parameter
        q (int): number of repetitions

    Returns:
        list[int], list[int], int: the best ordering, width profile and contraction width
    """
    bestOrder = None
    bestWidth = sys.maxsize
    bestNeighbors = []
    for i in range(q):
        order = []
        width = 0
        widths = []

        G_copy = G.copy()

        while G_copy.number_of_nodes() > 0:
            nodes = list(G_copy.nodes())
            weights = []
            prob = []
            # calculate probabilities for each node
            for v in nodes:
                num_neighbors = len(list(G_copy.neighbors(v)))
                w = math.exp(-1/tau * num_neighbors)
                weights.append(w)
            weightsSum = sum(weights)

            for w in weights:
                prob.append(w / weightsSum)

            v = random.choices(nodes, weights=prob)[0]

            width = max(width, len(list(G_copy.neighbors(v))))
            order.append(v)
            widths.append(len(list(G_copy.neighbors(v))))

            contract(G_copy, v)

        if width < bestWidth:
            bestWidth = width
            bestOrder = order
            bestNeighbors = widths
    return bestOrder, bestNeighbors, bestWidth

