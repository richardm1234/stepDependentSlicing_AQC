from ordering import *

def findOptimalS(G, widthProfile, order):
    """
    Find the optimal step s

    Args:
        G (nx.Graph): line graph
        widthProfile (list[int]): the degrees of each node
        order (list[int]): the initial ordering

    Returns:
        list[int], list[int], int, int, int: new ordering, new width profile, new contraction width,
        optimal step S and which vertices to slice
    """
    peak = widthProfile.index(max(widthProfile))
    minWidth = sys.maxsize
    optimalS = 0
    toSlice = None
    newWidthProfile = []
    newOrdering = []

    for s in range(peak):
        G_copy = G.copy()
        for v in order[:s]:
            contract(G_copy, v)
        maxNeighbors = sorted(G_copy.nodes(), key=lambda v: G_copy.degree(v), reverse=True)[0]
        G_copy.remove_node(maxNeighbors)
        newOrder, width, neighbors = greedy(G_copy)
        if width < minWidth:
            newOrdering = newOrder
            minWidth = width
            newWidthProfile = neighbors
            optimalS = s
            toSlice = maxNeighbors

    return newOrdering, newWidthProfile, minWidth, optimalS, toSlice

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




