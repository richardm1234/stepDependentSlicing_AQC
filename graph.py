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

def stepDependentSlicing(LG, order, widthProfile, n=1, r=1):
    """
    Build a schedule by running findOptimalS until n indices have been selected

    Args:
        LG (nx.Graph): line graph
        order (list[int]): ordering of which indices to contract based on rgreedy
        widthProfile (list[int]): width profile
        n (int): total number of indices to slice
        r (int): number of nodes to slice per step

    Returns:
        dict[int, list[int]]: optimal steps S and their corresponding nodes to slice
    """
    schedule = {}
    G_copy = LG.copy()

    for _ in range(n//r):
        newOrder, newWidthProfile, minWidth, optimalS, toSlice = findOptimalS(G_copy, widthProfile, order, 0, r)
        if toSlice is None:
            break
        schedule[optimalS] = toSlice
        for v in toSlice:
            G_copy.remove_node(v)
        order = newOrder
        widthProfile = newWidthProfile


    return schedule

def evaluateSchedule(G, order, widthProfile, schedule, tau=0.02, q=100):
    """
    Evaluate the schedule and re-order with rgreedy

    Args:
        G (nx.Graph): graph
        order (list[int]): the ordering
        widthProfile (list[int]): width profile
        schedule (dict[int, list[int]]): optimal steps S and their corresponding nodes to slice
        tau (float): sensitivity parameter for rgreedy
        q (int): repetitions of rgreedy

    Returns:
        list[int], list[int], int: ordering, padded width profile and the new contraction width
    """
    G_copy = G.copy()
    s = min(schedule.keys())
    for v in order[:s]:
        contract(G_copy, v)

    for sliceVars in schedule.values():
        for v in sliceVars:
            G_copy.remove_node(v)

    newOrder, newWidthProfile, newWidth = rgreedy(G_copy, tau, q)
    paddedWidthProfile = widthProfile[:s] + newWidthProfile
    return newOrder, paddedWidthProfile, newWidth





