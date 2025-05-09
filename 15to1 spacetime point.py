import qiskit
from matplotlib import pyplot as plt
from qiskit import QuantumCircuit
from qiskit.quantum_info import Clifford, Statevector
from qiskit_aer import AerSimulator
import numpy as np

def generatormeasurement(memory,target_qubits):
    # 计算每次测量的乘积
    products = []
    for binary_str in memory:
        # 注意：Qiskit 结果字符串为大端序（最高位在最左，对应经典寄存器13）
        # 例如 '10000000000000' 表示寄存器13=1，其他目标寄存器=0

        product = 1
        for qubit in target_qubits:
            # 计算目标经典寄存器在字符串中的位置
            cr_index = qubit  # 测量时量子比特 qubit 映射到经典寄存器 cr_index
            pos = 15 - cr_index  # 经典寄存器13对应字符串第0位（最左端）
            bit = int(binary_str[pos])
            product *= (-1) ** bit  # 若 bit=1 则乘积因子为 -1，否则为 1
        products.append(product)
    return products
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
c=qiskit.ClassicalRegister(16)
qc=QuantumCircuit(q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,
                  q16,c)
qc.h([0,1,3,7,15])
qc.barrier()
qc.cx(15,14)
qc.barrier()
for i in [8,9,10,11,12,13,14]:
    qc.cx(7,i)
qc.barrier()
for i in [4,5,6,11,12,13,14]:
    qc.cx(3,i)
qc.barrier()
for i in [2,5,6,9,10,13,14]:
    qc.cx(1,i)
qc.barrier()
for i in [2,4,6,8,10,12,14]:
    qc.cx(0,i)
qc.barrier()
for i in [2,4,5,8,9,11]:
    qc.cx(14,i)
qc.barrier()
allqubit=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
qc.tdg(allqubit)
g=[[3,4,5,6,7,8,9,10],
   [0,1,2,3,4,5,6,14],
   [1,2,3,4,9,10,11,12],
   [0,1,4,5,8,9,12,13]]
target_qubits=g[2]
G=[]
for i in range(len(g)):
    s=np.zeros(15).tolist()
    for j in range(len(g[i])):
        s[g[i][j]]=1
    G.append(s)
LX=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
LZ=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

qc.h(allqubit)

# 测量目标量子比特到对应的经典寄存器
qc.measure(allqubit,allqubit)

# 运行模拟器并记录内存
simulator = AerSimulator()
job = simulator.run(qc, shots=1000, memory=True)
memory = job.result().get_memory()

for i in range(len(g)):
    print(all(generatormeasurement(memory,g[i]))==1)
if all(generatormeasurement(memory,allqubit))==1:

qc.draw()
plt.show()



