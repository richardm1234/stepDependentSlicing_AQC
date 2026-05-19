import networkx as nx


def createGraph():
    """Generates a 3-regular graph"""
    G = nx.random_regular_graph(3, 10)
    nx.draw(G, with_labels = True)
    return G

def convertToLineGraph(G):
    LG = nx.line_graph(G)
    nx.draw(LG, with_labels = True)
    return LG