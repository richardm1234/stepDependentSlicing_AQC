import networkx as nx
from qiskit import QuantumCircuit

def createExampleCircuit(G):
    """Converts the 4 node graph to a QAOA circuit from the paper for testing purposes"""
    gamma = 0.5
    beta = 0.3
    circuit = QuantumCircuit(4)
    for i in range(4):
        circuit.h(i)

    for u,v in G.edges():
        circuit.rzz(2*gamma, u, v)

    for i in range(4):
        circuit.rx(2*beta, i)
    return circuit

def createNodeGraph():
    """Creates a basic 4 node graph for testing purposes"""
    G = nx.random_regular_graph(3, 4)
    return G


def createGraph():
    """Generates a 3-regular graph"""
    G = nx.random_regular_graph(3, 10)
    nx.draw(G, with_labels = True)
    return G

def convertToLineGraph(G):
    LG = nx.line_graph(G)
    nx.draw(LG, with_labels = True)
    return LG

