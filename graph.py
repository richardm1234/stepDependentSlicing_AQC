"""
This module provides functions for operating on a line graph
"""

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

def stepDependentSlicing(LG, order, widthProfile):
    """
    Build a schedule by running findOptimalS until n indices have been selected

    Args:
        LG (nx.Graph): line graph
        order (list[int]): ordering of which indices to contract based on rgreedy
        widthProfile (list[int]): width profile

    Returns:
        dict[int, list[int]], list[int], int: optimal step S and its corresponding node to slice, new width profile and new contraction width
    """

    newOrder, newWidthProfile, newWidth, optimalS, toSlice = findOptimalS(LG, widthProfile, order)
    if toSlice is None:
        return {}, widthProfile, max(widthProfile)
    return {optimalS: toSlice}, newWidthProfile, newWidth







