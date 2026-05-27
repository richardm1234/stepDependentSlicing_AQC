from ordering import *

def findOptimalS(G, widths, order):
    """
    Find the optimal step s

    Args:
        G (nx.Graph): line graph
        widths (list[int]): the degrees of each node
        order (list[int]): the initial ordering

    Returns:
        list[int], int, list[int], int, int: new ordering with less contraction width, the width profile
        optimal step S and which vertices to slice
    """
    peak = widths.index(max(widths))
    minCWidth = sys.maxsize
    optimalS = 0
    toSlice = None
    newWidths = []
    newOrdering = []

    for s in range(peak):
        G_copy = G.copy()
        for v in order[:s]:
            contract(G_copy, v)
        maxNeighbors = sorted(G_copy.nodes(), key=lambda v: G_copy.degree(v), reverse=True)[0]
        G_copy.remove_node(maxNeighbors)
        newOrder, width, neighbors = greedy(G_copy)
        if width < minCWidth:
            newOrdering = newOrder
            minCWidth = width
            newWidths = neighbors
            optimalS = s
            toSlice = maxNeighbors

    return newOrdering, minCWidth, newWidths, optimalS, toSlice

def stepDependentSlicing(LG, order, n=1, r=1):
    """
    Build a schedule from running findOptimalS n times

    Args:
        LG (nx.Graph): line graph
        order: ordering of which indices to contract based on rgreedy
        n: total number of indices to slice
        r: number of nodes to slice per step

    Returns:
        list[dict(int, int)]: list of optimal S and their corresponding slice nodes
    """
    pass




