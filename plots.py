import numpy as np
import matplotlib.pyplot as plt

def plotNeighbors(widths):
    """
    Plot the number of neighbors

    Args:
        widths: The number of neighbors
    """
    x = range(len(widths))
    neighbors = plt.subplot(1,2,1)
    neighbors.plot(x, widths, color='red', linestyle='-')
    neighbors.set_title("Contraction width")
    neighbors.set_xlabel("Steps")
    neighbors.set_ylabel("Number of neighbors")

    cost = plt.subplot(1,2,2)
    cost.plot(x, np.exp2(widths), color='red', linestyle='-')
    cost.set_title("Computational cost")
    cost.set_xlabel("Steps")

    plt.show()


def plotComparison(widths, newWidths, optimalS):
    """
    Plot a comparison between old and new contraction width in one plot

    Args:
        widths: Old contraction width
        newWidths: New contraction width
        optimalS: optimal step S, so contractions before that aren't cut off
    """
    paddedWidths = widths[:optimalS] + newWidths
    x1 = range(len(widths))
    x2 = range(len(paddedWidths))
    neighbors = plt.subplot(1, 2, 1)
    neighbors.plot(x1, widths, color='red', linestyle='-', label='Old Width')
    neighbors.plot(x2, paddedWidths, color='blue', linestyle='-', label='New Width')
    neighbors.set_title("Contraction width")
    neighbors.set_xlabel("Steps")
    neighbors.set_ylabel("Number of neighbors")
    neighbors.axvline(x=optimalS, color='green', linestyle='--', label='Slice')
    neighbors.legend()

    cost = plt.subplot(1, 2, 2)
    cost.plot(x1, np.exp2(widths), color='red', linestyle='-', label='Old Cost')
    cost.plot(x2, np.exp2(paddedWidths), color='blue', linestyle='-', label='New Cost')
    cost.set_title("Computational cost")
    cost.set_xlabel("Steps")
    cost.axvline(x=optimalS, color='green', linestyle='--', label='Slice')
    cost.legend()

    plt.show()