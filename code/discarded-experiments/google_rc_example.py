# This is a overly simplified implementation of Google's circuit as shown in Fig. 3

from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister

circ = QuantumCircuit(5,5)

circ.sx(1)
circ.sx(2)

circ.draw(output='mpl')