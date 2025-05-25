import qiskit
from qiskit import QuantumCircuit
import numpy as np
from qiskit.quantum_info import Statevector,Operator
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

qc=QuantumCircuit(16)
qc.t([11,12,13,14])
state1=state0.evolve(qc)
state=[]
state.append([state1])

for i in range(len(Z)):
    s=[]
    for j in range(len(state[i])):
        qc=QuantumCircuit(16)
        qc.z(Z[i])
        qc.z(10-i)
        sta=(state[i][j]+state[i][j].evolve(qc))/2
        s.append(sta)
    state.append(s)

state0=state[-1]

qc=QuantumCircuit(16)
def inver(A):
    B=[]
    for i in range(len(A)):
        B.append(16-A[i])
    return B
A=[2,16]
qc.x(inver(A))
qc.t([0,1,2,3,4,5,6,7,8,9,10])
state=[]
for i in range(len(state0)):
    state.append(state0[i].evolve(qc))

gener1=QuantumCircuit(16)
gener1.x(11)
gener2=QuantumCircuit(16)
gener2.x(12)
gener3=QuantumCircuit(16)
gener3.x(13)
gener4=QuantumCircuit(16)
gener4.x(14)
U = np.array([
    [0, np.exp(1j * np.pi / 4)],
    [np.exp(-1j * np.pi / 4), 0]
])
# 创建 Operator 对象
eigenTdg= Operator(U)
magic=QuantumCircuit(16)
magic.unitary(eigenTdg,15,label='EigenT')
tolerance = 1e-10  # 设置误差范围
pro=0
fidel=[]

finstate=[]
for i in range(1):
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

for i in range(len(finstate)):
    for j in range(len(finstate[i])):
        prostate1 = (finstate[i][j]+finstate[i][j].evolve(gener1))/2
        prostate2 = (prostate1 + prostate1.evolve(gener2)) / 2
        prostate3 = (prostate2 + prostate2.evolve(gener3)) / 2
        prostate4 = (prostate3 + prostate3.evolve(gener4)) / 2
        pro=pro+np.vdot(prostate4,prostate4)
        norm=np.linalg.norm(prostate4)
        prostate4=prostate4/norm
        fidestate=(prostate4+prostate4.evolve(magic))/2
        fide=np.linalg.norm(fidestate)
        if abs(fide-1)>tolerance:
            fidel.append((i,j,fide))
pro=pro*2**11

print(pro)
print(len(fidel))