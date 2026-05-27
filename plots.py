import numpy as np
import matplotlib.pyplot as plt

def plotNeighbors(widthProfile):
    """
    Plot the number of neighbors

    Args:
        widthProfile (list[int]): The number of neighbors
    """
    x = range(len(widthProfile))
    neighbors = plt.subplot(1,2,1)
    neighbors.plot(x, widthProfile, color='red', linestyle='-')
    neighbors.set_title("Width profile")
    neighbors.set_xlabel("Steps")
    neighbors.set_ylabel("Number of neighbors")

    cost = plt.subplot(1,2,2)
    cost.plot(x, np.exp2(widthProfile), color='red', linestyle='-')
    cost.set_title("Computational cost")
    cost.set_xlabel("Steps")

    plt.show()


def plotComparison(widthProfile, newWidthProfile, optimalS):
    """
    Plot a comparison between old and new contraction width in one plot

    Args:
        widthProfile (list[int]): Old contraction width
        newWidthProfile (list[int]): New contraction width
        optimalS (int): optimal step S
    """
    # ensures plot shows not only from step S onwards
    paddedWidths = widthProfile[:optimalS] + newWidthProfile

    neighbors = plt.subplot(1, 2, 1)
    neighbors.plot(range(len(widthProfile)), widthProfile, color='red', linestyle='-', label='Old Width')
    neighbors.plot(range(len(paddedWidths)), paddedWidths, color='blue', linestyle='-', label='New Width')
    neighbors.set_title("Contraction width")
    neighbors.set_xlabel("Steps")
    neighbors.set_ylabel("Number of neighbors")
    neighbors.axvline(x=optimalS, color='green', linestyle='--', label='Slice')
    neighbors.legend()

    cost = plt.subplot(1, 2, 2)
    cost.plot(range(len(widthProfile)), np.exp2(widthProfile), color='red', linestyle='-', label='Old Cost')
    cost.plot(range(len(paddedWidths)), np.exp2(paddedWidths), color='blue', linestyle='-', label='New Cost')
    cost.set_title("Computational cost")
    cost.set_xlabel("Steps")
    cost.axvline(x=optimalS, color='green', linestyle='--', label='Slice')
    cost.legend()

    plt.show()