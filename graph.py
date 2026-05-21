import networkx as nx
from qiskit import QuantumCircuit
import math

def createExampleCircuit(G) -> QuantumCircuit:
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

def convertToLineGraph(circuit: QuantumCircuit):
    LG = nx.Graph()
    for i in range(circuit.num_qubits):
        LG.add_node(i)
    return LG

def rgreedy(G, tau, q):
    p = 0.
    for i in range(q):
        for j in G.nodes:
            p = math.exp(-1/tau * j.neighbors)
    return p


