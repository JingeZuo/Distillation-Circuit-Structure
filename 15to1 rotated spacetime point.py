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

        sta=(state[i][j]-state[i][j].evolve(qc))/2
        qc=QuantumCircuit(16)
        qc.x(10-i)
        s.append(sta.evolve(qc))
    state.append(s)

state0=state[-1]

qc=QuantumCircuit(16)
qc.t([0,1,2,3,4,5,6,7,8,9,10])
state=[]
for i in range(len(state0)):
    state.append(state0[i].evolve(qc))

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
fidel=[]
tolerance = 1e-10  # 设置误差范围
#%%
finstate=[]
for i in range(102):
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
        prostate=(finstate[i][j]+finstate[i][j].evolve(gener))/2
        pro=pro+np.vdot(prostate,prostate)
        norm=np.linalg.norm(finstate[i][j])
        finstate[i][j]=finstate[i][j]/norm
        fidestate=(finstate[i][j]+finstate[i][j].evolve(magic))/2
        fide=np.linalg.norm(fidestate)
        if abs(fide-1)>tolerance:
            fidel.append((i,j))
del finstate
finstate=[]

for i in range(102,204):
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
        prostate=(finstate[i][j]+finstate[i][j].evolve(gener))/2
        pro=pro+np.vdot(prostate,prostate)
        norm=np.linalg.norm(finstate[i][j])
        finstate[i][j]=finstate[i][j]/norm
        fidestate=(finstate[i][j]+finstate[i][j].evolve(magic))/2
        fide=np.linalg.norm(fidestate)
        if abs(fide-1)>tolerance:
            fidel.append((i,j))
del finstate
finstate=[]
for i in range(204,306):
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
        prostate=(finstate[i][j]+finstate[i][j].evolve(gener))/2
        pro=pro+np.vdot(prostate,prostate)
        norm=np.linalg.norm(finstate[i][j])
        finstate[i][j]=finstate[i][j]/norm
        fidestate=(finstate[i][j]+finstate[i][j].evolve(magic))/2
        fide=np.linalg.norm(fidestate)
        if abs(fide-1)>tolerance:
            fidel.append((i,j))
del finstate
finstate=[]
for i in range(306,408):
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
        prostate=(finstate[i][j]+finstate[i][j].evolve(gener))/2
        pro=pro+np.vdot(prostate,prostate)
        norm=np.linalg.norm(finstate[i][j])
        finstate[i][j]=finstate[i][j]/norm
        fidestate=(finstate[i][j]+finstate[i][j].evolve(magic))/2
        fide=np.linalg.norm(fidestate)
        if abs(fide-1)>tolerance:
            fidel.append((i,j))
del finstate
finstate=[]
for i in range(408,510):
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
        prostate=(finstate[i][j]+finstate[i][j].evolve(gener))/2
        pro=pro+np.vdot(prostate,prostate)
        norm=np.linalg.norm(finstate[i][j])
        finstate[i][j]=finstate[i][j]/norm
        fidestate=(finstate[i][j]+finstate[i][j].evolve(magic))/2
        fide=np.linalg.norm(fidestate)
        if abs(fide-1)>tolerance:
            fidel.append((i,j))
del finstate
finstate=[]
for i in range(510,612):
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
        prostate=(finstate[i][j]+finstate[i][j].evolve(gener))/2
        pro=pro+np.vdot(prostate,prostate)
        norm=np.linalg.norm(finstate[i][j])
        finstate[i][j]=finstate[i][j]/norm
        fidestate=(finstate[i][j]+finstate[i][j].evolve(magic))/2
        fide=np.linalg.norm(fidestate)
        if abs(fide-1)>tolerance:
            fidel.append((i,j))
del finstate
finstate=[]
for i in range(612,714):
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
        prostate=(finstate[i][j]+finstate[i][j].evolve(gener))/2
        pro=pro+np.vdot(prostate,prostate)
        norm=np.linalg.norm(finstate[i][j])
        finstate[i][j]=finstate[i][j]/norm
        fidestate=(finstate[i][j]+finstate[i][j].evolve(magic))/2
        fide=np.linalg.norm(fidestate)
        if abs(fide-1)>tolerance:
            fidel.append((i,j))
del finstate
finstate = []
for i in range(714,816):
    state0 = []
    state0.append([state[i]])
    for j in range(len(Z)):
        s = []
        for k in range(len(state0[j])):
            qc = QuantumCircuit(16)
            qc.x(10 - j)
            sta = (state0[j][k] + state0[j][k].evolve(qc)) / 2
            s.append(sta)

            sta = (state0[j][k] - state0[j][k].evolve(qc)) / 2
            qc = QuantumCircuit(16)
            qc.z(Z[j])
            s.append(sta.evolve(qc))
        state0.append(s)
    finstate.append(state0[-1])

for i in range(len(finstate)):
    for j in range(len(finstate[i])):
        prostate = (finstate[i][j] + finstate[i][j].evolve(gener)) / 2
        pro = pro + np.vdot(prostate, prostate)
        norm = np.linalg.norm(finstate[i][j])
        finstate[i][j] = finstate[i][j] / norm
        fidestate = (finstate[i][j] + finstate[i][j].evolve(magic)) / 2
        fide = np.linalg.norm(fidestate)
        if abs(fide - 1) > tolerance:
            fidel.append((i,j))
del finstate
finstate=[]
for i in range(816,918):
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
        prostate=(finstate[i][j]+finstate[i][j].evolve(gener))/2
        pro=pro+np.vdot(prostate,prostate)
        norm=np.linalg.norm(finstate[i][j])
        finstate[i][j]=finstate[i][j]/norm
        fidestate=(finstate[i][j]+finstate[i][j].evolve(magic))/2
        fide=np.linalg.norm(fidestate)
        if abs(fide-1)>tolerance:
            fidel.append((i,j))
del finstate
finstate=[]
for i in range(918,1020):
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
        prostate=(finstate[i][j]+finstate[i][j].evolve(gener))/2
        pro=pro+np.vdot(prostate,prostate)
        norm=np.linalg.norm(finstate[i][j])
        finstate[i][j]=finstate[i][j]/norm
        fidestate=(finstate[i][j]+finstate[i][j].evolve(magic))/2
        fide=np.linalg.norm(fidestate)
        if abs(fide-1)>tolerance:
            fidel.append((i,j))
del finstate
finstate=[]
for i in range(1020,1122):
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
        prostate=(finstate[i][j]+finstate[i][j].evolve(gener))/2
        pro=pro+np.vdot(prostate,prostate)
        norm=np.linalg.norm(finstate[i][j])
        finstate[i][j]=finstate[i][j]/norm
        fidestate=(finstate[i][j]+finstate[i][j].evolve(magic))/2
        fide=np.linalg.norm(fidestate)
        if abs(fide-1)>tolerance:
            fidel.append((i,j))
del finstate
finstate=[]
for i in range(1122,1224):
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
        prostate=(finstate[i][j]+finstate[i][j].evolve(gener))/2
        pro=pro+np.vdot(prostate,prostate)
        norm=np.linalg.norm(finstate[i][j])
        finstate[i][j]=finstate[i][j]/norm
        fidestate=(finstate[i][j]+finstate[i][j].evolve(magic))/2
        fide=np.linalg.norm(fidestate)
        if abs(fide-1)>tolerance:
            fidel.append((i,j))
del finstate
finstate=[]
for i in range(1224,1326):
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
        prostate=(finstate[i][j]+finstate[i][j].evolve(gener))/2
        pro=pro+np.vdot(prostate,prostate)
        norm=np.linalg.norm(finstate[i][j])
        finstate[i][j]=finstate[i][j]/norm
        fidestate=(finstate[i][j]+finstate[i][j].evolve(magic))/2
        fide=np.linalg.norm(fidestate)
        if abs(fide-1)>tolerance:
            fidel.append((i,j))
del finstate
finstate=[]
for i in range(1326,1428):
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
        prostate=(finstate[i][j]+finstate[i][j].evolve(gener))/2
        pro=pro+np.vdot(prostate,prostate)
        norm=np.linalg.norm(finstate[i][j])
        finstate[i][j]=finstate[i][j]/norm
        fidestate=(finstate[i][j]+finstate[i][j].evolve(magic))/2
        fide=np.linalg.norm(fidestate)
        if abs(fide-1)>tolerance:
            fidel.append((i,j))
del finstate
finstate=[]
for i in range(1428,1530):
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
        prostate=(finstate[i][j]+finstate[i][j].evolve(gener))/2
        pro=pro+np.vdot(prostate,prostate)
        norm=np.linalg.norm(finstate[i][j])
        finstate[i][j]=finstate[i][j]/norm
        fidestate=(finstate[i][j]+finstate[i][j].evolve(magic))/2
        fide=np.linalg.norm(fidestate)
        if abs(fide-1)>tolerance:
            fidel.append((i,j))
del finstate
finstate = []
for i in range(1530,1632):
    state0 = []
    state0.append([state[i]])
    for j in range(len(Z)):
        s = []
        for k in range(len(state0[j])):
            qc = QuantumCircuit(16)
            qc.x(10 - j)
            sta = (state0[j][k] + state0[j][k].evolve(qc)) / 2
            s.append(sta)

            sta = (state0[j][k] - state0[j][k].evolve(qc)) / 2
            qc = QuantumCircuit(16)
            qc.z(Z[j])
            s.append(sta.evolve(qc))
        state0.append(s)
    finstate.append(state0[-1])

for i in range(len(finstate)):
    for j in range(len(finstate[i])):
        prostate = (finstate[i][j] + finstate[i][j].evolve(gener)) / 2
        pro = pro + np.vdot(prostate, prostate)
        norm = np.linalg.norm(finstate[i][j])
        finstate[i][j] = finstate[i][j] / norm
        fidestate = (finstate[i][j] + finstate[i][j].evolve(magic)) / 2
        fide = np.linalg.norm(fidestate)
        if abs(fide - 1) > tolerance:
            fidel.append((i,j))
del finstate
finstate=[]
for i in range(1632,1734):
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
        prostate=(finstate[i][j]+finstate[i][j].evolve(gener))/2
        pro=pro+np.vdot(prostate,prostate)
        norm=np.linalg.norm(finstate[i][j])
        finstate[i][j]=finstate[i][j]/norm
        fidestate=(finstate[i][j]+finstate[i][j].evolve(magic))/2
        fide=np.linalg.norm(fidestate)
        if abs(fide-1)>tolerance:
            fidel.append((i,j))
del finstate
finstate=[]
for i in range(1734,1836):
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
        prostate=(finstate[i][j]+finstate[i][j].evolve(gener))/2
        pro=pro+np.vdot(prostate,prostate)
        norm=np.linalg.norm(finstate[i][j])
        finstate[i][j]=finstate[i][j]/norm
        fidestate=(finstate[i][j]+finstate[i][j].evolve(magic))/2
        fide=np.linalg.norm(fidestate)
        if abs(fide-1)>tolerance:
            fidel.append((i,j))
del finstate
finstate=[]
for i in range(1836,1938):
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
        prostate=(finstate[i][j]+finstate[i][j].evolve(gener))/2
        pro=pro+np.vdot(prostate,prostate)
        norm=np.linalg.norm(finstate[i][j])
        finstate[i][j]=finstate[i][j]/norm
        fidestate=(finstate[i][j]+finstate[i][j].evolve(magic))/2
        fide=np.linalg.norm(fidestate)
        if abs(fide-1)>tolerance:
            fidel.append((i,j))
del finstate
finstate=[]
for i in range(1938,2040):
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
        prostate=(finstate[i][j]+finstate[i][j].evolve(gener))/2
        pro=pro+np.vdot(prostate,prostate)
        norm=np.linalg.norm(finstate[i][j])
        finstate[i][j]=finstate[i][j]/norm
        fidestate=(finstate[i][j]+finstate[i][j].evolve(magic))/2
        fide=np.linalg.norm(fidestate)
        if abs(fide-1)>tolerance:
            fidel.append((i,j))
del finstate
finstate=[]
for i in range(2040,2048):
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
        prostate=(finstate[i][j]+finstate[i][j].evolve(gener))/2
        pro=pro+np.vdot(prostate,prostate)
        norm=np.linalg.norm(finstate[i][j])
        finstate[i][j]=finstate[i][j]/norm
        fidestate=(finstate[i][j]+finstate[i][j].evolve(magic))/2
        fide=np.linalg.norm(fidestate)
        if abs(fide-1)>tolerance:
            fidel.append((i,j))
print(pro)
print(len(fidel))
#%%
import sys

# 假设你的 list 名字是 finstate，并且已经存在了
# finstate = [...]  # 这个 list 里有 2048 个 statevector

# 计算每个元素的大小，然后加起来
total_size = sum(sys.getsizeof(item) for item in finstate[0])

# 转换成 MB（1 MB = 1024 * 1024 字节）
mb = total_size / (1024 ** 2)

print(f"finstate 总共占用内存大约为: {mb:.2f} MB")