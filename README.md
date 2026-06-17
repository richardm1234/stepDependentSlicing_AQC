# stepDependentSlicing_AQC

Step-dependent slicing for tensor network contraction of QAOA circuits

Developed as part of the *Seminar: Advanced Topics in Quantum Computing, TU Munich*.

Implements parts of the approach from: **Lykov et al. — Tensor Network Quantum Simulator With Step-Dependent Parallelization**.

## Overview

This project implements step-dependent slicing for tensor network contraction to simulate QAOA circuits more efficiently.

## Repository structure

```
.
├── graph.py          # Graph construction and QAOA circuit utilities
├── conversion.py     # Conversion between circuit and tensor network representations
├── ordering.py       # Contraction ordering and step-dependent slicing logic
├── plots.py          # Visualisation of contraction width and slicing results
├── demo.ipynb        # Interactive Jupyter notebook demo
├── requirements.txt  # Python dependencies
└── README.md
```

## Requirements

- Python 3.9+
- [NetworkX](https://networkx.org/)
- [Qiskit](https://qiskit.org/)
- NumPy, Matplotlib

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the interactive demo:

```bash
jupyter notebook demo.ipynb
```

Or use the modules directly:

```python
from conversion import *
from ordering import rgreedy
from graph import stepDependentSlicing
from plots import plotComparison

G = createGraph(10)
circuit = convertToCircuit(G)
LG = convertToLineGraph(circuit)

order, widths, width = rgreedy(LG, 0.02, 200)
schedule, newWidths, newWidth = stepDependentSlicing(LG, order, widths)
plotComparison(widths, newWidths, schedule)
```

## Citation

If you use this code, please cite this repository using the metadata in `CITATION.cff`.

The underlying method is described in:
> Lykov et al. — Tensor Network Quantum Simulator With Step-Dependent Parallelization

## License

MIT © 2026 Richard Mayer
