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

qc.h([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
state0=Statevector.from_instruction(qc)
Z=[[14,13,12],
   [15,14,13],
   [15,14,12],
   [15,13,12],
   [15,12,11],
   [15,14,11],
   [15,13,11],
   [15,14,13,12,11],
   [13,12,11],
   [14,12,11],
   [14,13,11]]
qc.draw()
plt.show()
print(len(Z))
#%%
qc=QuantumCircuit(16)
qc.t([11,12,13,14])
state1=state0.evolve(qc)
state=[]
state.append([state1])
print(len(state[0]))
#%%
for i in range(len(Z)):
    s=[]
    for j in range(len(state[i])):
        qc=QuantumCircuit(16)
        qc.z(Z[i])
        qc.z(10-i)
        sta=(state[i][j]+state[i][j].evolve(qc))/2
        s.append(sta)

        sta=(state[i][j]-state[i][j].evolve(qc))/2
        qc=QuantumCircuit(16)
        qc.x(10-i)
        s.append(sta.evolve(qc))
    state.append(s)
print(len(state))
#%%
state0=state[-1]

qc=QuantumCircuit(16)
qc.t([0,1,2,3,4,5,6,7,8,9,10])
state=[]
for i in range(len(state0)):
    state.append(state0[i].evolve(qc))
print(len(state))

#%%
finstate=[]
for i in range(len(state)):
    state0 = []
    state0.append([state[i]])
    for j in range(len(Z)):
        s=[]
        for k in range(len(state0[j])):
            qc=QuantumCircuit(16)
            qc.x(10-j)
            sta=(state0[j][k]+state0[j][k].evolve(qc))/2
            s.append(sta)

            sta = (state0[j][k] - state0[j][k].evolve(qc)) / 2
            qc=QuantumCircuit(16)
            qc.z(Z[j])
            s.append(sta.evolve(qc))
        state0.append(s)
    finstate.append(state0[-1])
print(len(finstate))

#%%
gener=QuantumCircuit(16)
gener.x([11,12,13,14])
U = np.array([
    [0, np.exp(1j * np.pi / 4)],
    [np.exp(-1j * np.pi / 4), 0]
])
# 创建 Operator 对象
eigenTdg= Operator(U)
magic=QuantumCircuit(16)
magic.unitary(eigenTdg,15,label='EigenT')
pro=0
for i in range(len(finstate)):
    for j in range(len(finstate[i])):
        prostate=(finstate[i][j]+finstate[i][j].evolve(gener))/2
        pro=pro+np.vdot(prostate,prostate)
s=finstate[0][0]
ns=np.linalg.norm(s)
s=s/ns

fide=np.linalg.norm((s+s.evolve(magic))/2)
print(fide)
print(pro)



