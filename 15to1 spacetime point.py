import qiskit
from matplotlib import pyplot as plt
from qiskit import QuantumCircuit, transpile
from qiskit.quantum_info import Clifford, Statevector
from qiskit_aer import AerSimulator
import numpy as np

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

c1=qiskit.ClassicalRegister(1,'c1')
c2=qiskit.ClassicalRegister(1,'c2')
c3=qiskit.ClassicalRegister(1,'c3')
c4=qiskit.ClassicalRegister(1,'c4')
c5=qiskit.ClassicalRegister(1,'c5')
c6=qiskit.ClassicalRegister(1,'c6')
c7=qiskit.ClassicalRegister(1,'c7')
c8=qiskit.ClassicalRegister(1,'c8')
c9=qiskit.ClassicalRegister(1,'c9')
c10=qiskit.ClassicalRegister(1,'c10')
c11=qiskit.ClassicalRegister(1,'c11')
c12=qiskit.ClassicalRegister(1,'c12')
c13=qiskit.ClassicalRegister(1,'c13')
c14=qiskit.ClassicalRegister(1,'c14')
c15=qiskit.ClassicalRegister(1,'c15')
c16=qiskit.ClassicalRegister(1,'c16')
qp=qiskit.QuantumRegister(1,'qp')
cp=qiskit.ClassicalRegister(1,'cp')
qc=QuantumCircuit(q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,qp,
                  c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15,c16,cp)
qreg=[q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15]
creg=[c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15]
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
allqubit=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
qc.tdg(allqubit)
g=[[3,4,5,6,7,8,9,10],
   [0,1,2,3,4,5,6,14],
   [1,2,3,4,9,10,11,12],
   [0,1,4,5,8,9,12,13]]
qc.h(allqubit)
for q_reg, c_reg in zip(qreg, creg):
    qc.measure(q_reg[0], c_reg[0])
for c in creg:
    with qc.if_test((c, 1)):  # 新版条件语法（寄存器对象 + 目标值）
        qc.x(qp)
qc.measure(qp,cp)
with qc.if_test((cp,1)):
    qc.z(q16)
qc.tdg(15)
qc.h(15)
qc.measure(q16,c16)
 # q_reg[0] 是唯一的量子位，c_reg[0] 是唯一的经典位
# 3. 编译并运行电路
# ---------------------------
# 创建模拟器后端
backend = AerSimulator()  # 自动支持动态电路
# 显式编译电路（替代旧版 compile() 方法）
transpiled_circuit = transpile(qc, backend)  # 关键修复点
# 执行电路
job = backend.run(transpiled_circuit, shots=20)
result = job.result()
counts = result.get_counts()
qc.draw()
plt.show()
# ---------------------------
# 4. 结果输出
# ---------------------------
#list转换
counts_list = [[int(c) for c in key.split()] for key in counts]
#logicalX,generatorX
for i in range(len(counts_list)):
    l=0
    for j in range(len(counts_list[i])-1):
        l=l+counts_list[i][len(counts_list[i])-1-j]
    for m in range(len(g)):
        s = 0
        for n in range(len(g[m])):
            s=s+counts_list[i][len(counts_list[i])-1-g[m][n]]
        print('s',m,s%2)
    print(l%2)


