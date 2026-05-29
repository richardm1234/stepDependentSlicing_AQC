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

    fig, plots = plt.subplots(2,2)
    neighbors = plots[0,0]
    neighbors.plot(range(len(widthProfile)), widthProfile, color='red', linestyle='-', label='Old Width')
    neighbors.set_title("Contraction width before")
    neighbors.set_xlabel("Steps")
    neighbors.set_ylabel("Number of neighbors")
    neighbors.axvline(x=optimalS, color='green', linestyle='--', label='Slice')
    #neighbors.legend()

    newNeighbors = plots[0,1]
    newNeighbors.plot(range(len(paddedWidths)), paddedWidths, color='blue', linestyle='-', label='New Width')
    newNeighbors.set_title("Contraction width after")
    newNeighbors.set_xlabel("Steps")
    newNeighbors.set_ylabel("Number of neighbors")
    newNeighbors.axvline(x=optimalS, color='green', linestyle='--', label='Slice')

    cost = plots[1,0]
    cost.plot(range(len(widthProfile)), np.exp2(widthProfile), color='red', linestyle='-', label='Old Cost')
    cost.set_title("Computational cost before")
    cost.set_xlabel("Steps")
    cost.axvline(x=optimalS, color='green', linestyle='--', label='Slice')
    #cost.legend()

    newCost = plots[1,1]
    newCost.plot(range(len(paddedWidths)), np.exp2(paddedWidths), color='blue', linestyle='-', label='New Cost')
    newCost.set_title("Computational cost after")
    newCost.set_xlabel("Steps")
    newCost.axvline(x=optimalS, color='green', linestyle='--', label='Slice')

    plt.show()