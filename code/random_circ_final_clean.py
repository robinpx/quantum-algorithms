#!/usr/bin/env python
# coding: utf-8

# In[104]:


import numpy as np
from qiskit import QuantumCircuit, transpile, assemble, IBMQ, Aer
from qiskit.visualization import plot_histogram
from qiskit.providers.aer import QasmSimulator
from qiskit.providers.aer.noise import NoiseModel

total_qubits = 5
circ = QuantumCircuit(total_qubits) # quantum circuit of 3 qubits
circ.h(0) # add h to put qubit into superposition
circ.cx(0, range(1, 5)) # add cnot gate
circ.measure_all()
circ.draw("mpl")


# In[57]:


# run on QASM Simulator 
# transpile quantum circuit to low-level QASM instructions for backend
# execute the circuit on the qasm simulator, given number of shots (run repeats)

qasm_sim = QasmSimulator()
shots = 1024
qc_compiled = transpile(circ, qasm_sim) 

job_sim = qasm_sim.run(qc_compiled, shots=shots)
result_sim = job_sim.result()
counts = result_sim.get_counts(qc_compiled)

print(counts)


# In[58]:


plot_histogram(counts)


# In[120]:


provider=IBMQ.load_account()
provider = IBMQ.get_provider(hub='ibm-q')
provider.backends()
# show options for backends


# In[121]:


ibmq_backend = provider.get_backend('ibmq_quito')
noise_model = NoiseModel.from_backend(ibmq_backend)


# In[122]:


transpiled_circ = transpile(circ, ibmq_backend, optimization_level=3)
transpiled_circ.draw('mpl')


# In[123]:


assembled_circ = assemble(transpiled_circ, shots=shots)
sim_job = qasm_sim.run(transpiled_circ, noise_model=noise_model)
sim_result = sim_job.result()
sim_counts = sim_result.get_counts()
plot_histogram(sim_counts)


# In[ ]:


real_job = ibmq_backend.run(assembled_circ)
# real_job = execute(transpiled_circ, ibmq_backend, shots=shots)
real_result = real_job.result()
real_counts = real_result.get_counts()

plot_histogram([sim_counts, real_counts], bar_labels=False)


# In[72]:


from math import log

# probability and entropy of each event 
vn_entropy = {}
for k,v in counts.items():
    p = v/shots
    # print("probability of ", k," is ",p)
    # calculate entropy
    entropy = -sum([p * log(p) for _ in range(shots)])
    vn_entropy[k] = [entropy]
    # print the result
    # print('entropy: %.3f nats' % entropy)

print(vn_entropy)


# In[74]:


# import matplotlib.pyplot as plt

# time = np.arange(0.001, 1., 0.01)

# plt.xlabel('time')
# plt.ylabel('entropy')
# plt.title('stuff')
# plt.plot(time, vn_entropy, color='tab:blue')
# plt.show()


# In[ ]:





# In[ ]:




