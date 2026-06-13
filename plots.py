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


def plotComparison(widthProfile, newWidthProfile, schedule):
    """
    Plot a comparison between old and new contraction width in one plot

    Args:
        widthProfile (list[int]): Old contraction width
        newWidthProfile (list[int]): New contraction width
        schedule (dict[int, list[int]]): optimal steps S and their corresponding nodes to slice
    """
    # ensures plot shows not only from step S onwards
    paddedWidths = widthProfile[:min(schedule.keys())] + newWidthProfile

    fig, plots = plt.subplots(2,2, sharey='col')

    # Contraction width plots
    neighbors = plots[0,0]
    neighbors.plot(range(len(widthProfile)), widthProfile, color='red', linestyle='-', label='Old Width')
    neighbors.set_title("Contraction width before")
    neighbors.set_xlabel("Steps")
    neighbors.set_ylabel("Number of neighbors")


    newNeighbors = plots[1,0]
    newNeighbors.plot(range(len(paddedWidths)), paddedWidths, color='blue', linestyle='-', label='New Width')
    newNeighbors.set_title("Contraction width after")
    newNeighbors.set_xlabel("Steps")
    newNeighbors.set_ylabel("Number of neighbors")


    # Cost plots
    cost = plots[0,1]
    cost.plot(range(len(widthProfile)), np.exp2(widthProfile), color='red', linestyle='-', label='Old Cost')
    cost.set_title("Computational cost before")
    cost.set_xlabel("Steps")


    newCost = plots[1,1]
    newCost.plot(range(len(paddedWidths)), np.exp2(paddedWidths), color='blue', linestyle='-', label='New Cost')
    newCost.set_title("Computational cost after")
    newCost.set_xlabel("Steps")


    for s in schedule.keys():
        neighbors.axvline(x=s, color='green', linestyle='--', label='Slice')
        newNeighbors.axvline(x=s, color='green', linestyle='--', label='Slice')
        cost.axvline(x=s, color='green', linestyle='--', label='Slice')
        newCost.axvline(x=s, color='green', linestyle='--', label='Slice')

    plt.tight_layout()
    plt.show()
