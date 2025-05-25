import multiprocessing
import numpy as np
import qiskit
from qiskit import QuantumCircuit
import numpy as np
from qiskit.quantum_info import Statevector,Operator

import qiskit
from qiskit import QuantumCircuit
import numpy as np
from qiskit.quantum_info import Statevector,Operator
from itertools import repeat
import time

import qiskit
from qiskit import QuantumCircuit
import numpy as np
from qiskit.quantum_info import Statevector,Operator


qc=QuantumCircuit(16)

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
tolerance = 1e-10  # 设置误差范围

def worker(start, step):
    """单个进程的处理函数"""
    finstate = []
    pro=0
    fidel=[]
    for i in range(start,start+step):
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
                fidel.append((i, j))
    return (pro, fidel)

if __name__ == '__main__':
    # 配置参数
    total_processes = 64  # 总进程数
    step = 32  # 每个进程处理10个数
    starts = [i * step for i in range(total_processes)]  # 生成0,10,20,...,630

    # 创建进程池（推荐设为CPU核心数）
    with multiprocessing.Pool(processes=64) as pool:  # 8核机器
        # 批量提交任务 (starts, 固定step, pro, fidel)
        results=pool.starmap(worker, zip(starts, repeat(step)))
        # 合并结果
    total_pro = 0
    total_fidel = []

    # 遍历每个进程的结果
    for pro_local, fidel_local in results:
        total_pro += pro_local  # 累加pro值
        total_fidel.extend(fidel_local)  # 合并列表

    print('提纯成功率', total_pro)
    print("失真向量数", len(total_fidel))


