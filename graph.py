import networkx as nx

def createGraph():
    G = nx.random_regular_graph(3, 10)
    nx.draw(G)