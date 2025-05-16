import qiskit
from matplotlib import pyplot as plt
from qiskit import QuantumCircuit, transpile
from qiskit.circuit.library import XGate
from qiskit.quantum_info import Clifford, Statevector, DensityMatrix
from qiskit_aer import AerSimulator
import numpy as np
from qiskit.quantum_info import SuperOp,Statevector,Pauli,DensityMatrix,Operator,partial_trace,Clifford,PTM,Choi
q1= qiskit.QuantumRegister(1, '|0>\u2081')
q2= qiskit.QuantumRegister(1, '|0>\u2082')
q3= qiskit.QuantumRegister(1, '|0>\u2083')
q4= qiskit.QuantumRegister(1, '|0>\u2084')
q5= qiskit.QuantumRegister(1, '|0>\u2085')
q6= qiskit.QuantumRegister(1, '|0>\u2086')
q7= qiskit.QuantumRegister(1, '|0>\u2087')
q8= qiskit.QuantumRegister(1, '|0>\u2088')
q9= qiskit.QuantumRegister(1, '|0>\u2089')
q10= qiskit.QuantumRegister(1, '|0>\u2081\u2080')
q11= qiskit.QuantumRegister(1, '|0>\u2081\u2081')
q12= qiskit.QuantumRegister(1, '|0>\u2081\u2082')
q13= qiskit.QuantumRegister(1, '|0>\u2081\u2083')
q14= qiskit.QuantumRegister(1, '|0>\u2081\u2084')
q15= qiskit.QuantumRegister(1, '|0>\u2081\u2085')
q16= qiskit.QuantumRegister(1, '|0>\u2081\u2086')

qc=QuantumCircuit(q16,q15,q14,q13,q12,q11,q10,q9,q8,q7,q6,q5,q4,q3,q2,q1)

qc.h([15,14,12,8,0])
qc.barrier()
qc.cx(0,1)
qc.barrier()
for i in [7,6,5,4,3,2,1]:
    qc.cx(8,i)
qc.barrier()
for i in [11,10,9,4,3,2,1]:
    qc.cx(12,i)
qc.barrier()
for i in [13,10,9,6,5,2,1]:
    qc.cx(14,i)
qc.barrier()
for i in [13,11,9,7,5,3,1]:
    qc.cx(15,i)
qc.barrier()
for i in [13,11,10,7,6,4]:
    qc.cx(1,i)
qc.barrier()
allqubit=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
qc.tdg(allqubit)
g=[[12,11,10,9,8,7,6,5],
   [15,14,13,12,11,10,9,1],
   [14,13,12,11,6,5,4,3],
   [15,14,11,10,7,6,3,2]]

state0=Statevector.from_instruction(qc)
qc.barrier()
qc.draw()
plt.show()
#%%
#stablizer1
qc.x(g[0])
state1=(state0+Statevector.from_instruction(qc))/2
qc.barrier()
qc.draw()
plt.show()
#%%
#stablizer2
qc.x(g[1])
state2=(state1+Statevector.from_instruction(qc))/2
qc.barrier()
qc.draw()
plt.show()
#%%
#stablizer3
qc.x(g[2])
state3=(state2+Statevector.from_instruction(qc))/2
qc.barrier()
qc.draw()
plt.show()
#%%
#stablizer4
qc.x(g[3])
state4=(state3+Statevector.from_instruction(qc))/2
qc.barrier()
qc.draw()
plt.show()
#%%
#Logical X+1
qc.x(allqubit)
state=Statevector.from_instruction(qc)
stateLplus=(state4+state)/2
normLplus=np.linalg.norm(stateLplus.data)
proLplus=abs(normLplus)**2
print(proLplus)
qc.barrier()
qc.draw()
plt.show()
#%%
#Logical X-1
q=QuantumCircuit(16)
q.z(0)
stateLm=(state4-state)/2
normLminus=np.linalg.norm(stateLm.data)
stateLminus=(stateLm).evolve(q)
proLminus=abs(normLminus)**2
print(proLminus)
#%%
# 定义矩阵
q=QuantumCircuit(16)
U = np.array([
    [0, np.exp(-1j * np.pi / 4)],
    [np.exp(1j * np.pi / 4), 0]
])
# 创建 Operator 对象
eigenT= Operator(U)
q.unitary(eigenT,0,label='EigenT')
magicplus=(stateLplus+stateLplus.evolve(q))/2
magicminus=(stateLminus+stateLminus.evolve(q))/2
promplus=abs(np.linalg.norm(magicplus.data))**2
promminus=abs(np.linalg.norm(magicminus.data))**2
print(promplus)
print(promminus)
print(promplus+promminus)
#%%
is_equiv = state4.equiv(state3)
print(f"等价性判断: {is_equiv}")


