from ordering import *

def findOptimalS(G, widthProfile, order, startS=0, r=1):
    """
    Find the optimal step s

    Args:
        G (nx.Graph): line graph
        widthProfile (list[int]): the degrees of each node
        order (list[int]): the initial ordering
        startS: the search for optimal S begins here
        r: number of vertices to slices at step S

    Returns:
        list[int], list[int], int, int, list[int]: new ordering, new width profile, new contraction width,
        optimal step S and the r vertices to slice at step S
    """
    peak = widthProfile.index(max(widthProfile))
    minWidth = sys.maxsize
    optimalS = 0
    toSlice = None
    newWidthProfile = []
    newOrdering = []

    for s in range(startS, peak):
        G_copy = G.copy()
        for v in order[:s]:
            contract(G_copy, v)
        sortedDeg = sorted(G_copy.nodes(), key=lambda v: G_copy.degree(v), reverse=True)
        minR = min(len(sortedDeg), r)
        rMaxNeighbors = sortedDeg[:minR]
        for v in rMaxNeighbors:
            G_copy.remove_node(v)
        newOrder, neighbors, width = greedy(G_copy)
        if width < minWidth:
            newOrdering = newOrder
            minWidth = width
            newWidthProfile = neighbors
            optimalS = s
            toSlice = rMaxNeighbors

    return newOrdering, newWidthProfile, minWidth, optimalS, toSlice

def stepDependentSlicing(LG, order, widthProfile, n=2, r=1):
    """
    Build a schedule from running findOptimalS n times

    Args:
        LG (nx.Graph): line graph
        order (list[int]): ordering of which indices to contract based on rgreedy
        widthProfile (list[int]): width profile
        n (int): total number of indices to slice
        r (int): number of nodes to slice per step

    Returns:
        dict[int, list[int]]: optimal S and their corresponding slice nodes
    """
    schedule = {}
    startS = 0
    for _ in range(n//r):
        newOrder, newWidthProfile, minWidth, optimalS, toSlice = findOptimalS(LG, widthProfile, order, startS, r)
        if toSlice is None:
            break
        schedule[optimalS] = toSlice
        order = newOrder
        widthProfile = newWidthProfile
        startS = 0


    return schedule





