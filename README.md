# Complexity and Demonstration of Quantum Supremacy Algorithms
Code and documentation for our short-duration research on "Complexity and Demonstration of Quantum Supremacy Algorithms."

We are developing a series of experiments using Qiskit and IBM Q to run a quantum supremacy demonstration and analyze its complexity.

# Built With
* [IBM Q](https://quantum-computing.ibm.com/)
* [Qiskit](https://qiskit.org/) (Python)
* [Jupyter Notebook](https://jupyter.org/)

# Overview
For our capstone, we produced code to generate a random quantum circuit with single-qubit gates, Pauli-X, Y, Z, and Hadamard gates, and a multi-qubit gate, CNOT gate with IBM Q, Qiskit, and Python. We managed to perform random circuit sampling on our random quantum circuit, producing a series of output distributions from the measured outcome of an instance of a random quantum circuit at a particular circuit depth. By calculating the probabilities from its output distribution, we calculated the Von Neumann entropy of a generated random quantum circuit. We use Qiskit Aer's QASMSimulator with a simulated IBM Q backend as well as tested our circuit with IBM Q's Quito. We analyzed the entropy of our random quantum circuit to a circuit depth of 201, and showed that our circuit had an entropy of E  ≈ 3.5 at a circuit depth of L  ≈ 50. 

For our next steps, we recommend running it further on the real IBM Q's Quito,
looking at the convergence to the Porter-Thomas distribution in order to further our understanding of cross-entropy difference in comparsion to the ideal circuit output and its role in cross-entropy benchmarking. 

Below is a generalized flowchart produced from our research and current understanding of the material.
<img src="/documentation/General_flowchart.png" width="50%" />

### [code](./code) &nbsp; [documentation](./documentation/DOCS.md)

# Acknowledgements
* [Circuit Basics](https://qiskit.org/documentation/tutorials/circuits/01_circuit_basics.html)
* [Qiskit Textbook](https://qiskit.org/textbook)
* [Qiskit Github](https://github.com/Qiskit/qiskit-terra)