from qiskit import QuantumCircuit,transpile
from qiskit.quantum_info import SuperOp,Statevector,Pauli,DensityMatrix,Operator,partial_trace,Clifford,PTM,Choi
# from qiskit_aer import AerSimulator
from qiskit_aer.noise import NoiseModel,pauli_error,depolarizing_error
# from qiskit_aer.utils import insert_noise
# from qiskit.synthesis import generate_basic_approximations
from qiskit.circuit.library import TGate,TdgGate,SGate,SdgGate
# from qiskit.circuit import QuantumRegister,Qubit
import numpy as np
import matplotlib.pyplot as plt
import random,time,pickle

tol=1e-18

def Twirling(noise):
    X = Pauli('X').to_matrix()
    Y = Pauli('Y').to_matrix()
    I = Pauli('I').to_matrix()
    # 计算 (X + Y) / sqrt(2)
    op = (X + Y)/ np.sqrt(2)
    return (np.kron(I,I)+noise@np.kron(op.conj(),op))/2

def Mx1(n,flag):
    str0 = ''
    for i in range(n-1):
        str0+='I'
    X = Operator.from_label(str0+'X')
    I = Operator.from_label(str0+'I')
    if flag == 0 :
        return (X + I)/2
    else:
        return (-X + I)/2
    
def Mx2(n,flag):
    str0 = ''
    for i in range(n-1):
        str0+='I'
    X = Operator.from_label('X'+str0)
    I = Operator.from_label('I'+str0)
    if flag == 0 :
        return (X + I)/2
    else:
        return (-X + I)/2
    
# str0 = 'I'
# XR1 = Operator.from_label(str0 + 'IXXXXXXIIII')
# XR2 = Operator.from_label(str0 + 'XXXXIIIIIIX')
# XR3 = Operator.from_label(str0 + 'XXIIIXXXXII')
# XR4 = Operator.from_label(str0 + 'IXXIXXIIXXI')
# def Mx3(siglist):
#     Id = Operator.from_label('IIIIIIIIIIII')
#     flag = siglist[::-1]
#     if (flag[0]+flag[1])%2 ==0:
#         pro4 = (Id + XR4)/2
#     else:
#         pro4 = (Id - XR4)/2
#     if (flag[1]+flag[2])%2 ==0:
#         pro3 = (Id + XR3)/2
#     else:
#         pro3 = (Id - XR3)/2
#     if (flag[0]+flag[1]+flag[2])%2 ==0:
#         pro2 = (Id + XR2)/2
#     else:
#         pro2 = (Id - XR2)/2
#     if (flag[2]+flag[3])%2 ==0:
#         pro1 = (Id + XR1)/2
#     else:
#         pro1 = (Id - XR1)/2
#     return pro1@pro2@pro3@pro4

def Mx3(siglist):
    flag = siglist[::-1]
    title = './Prepare/Projector_'
    with open(title+str(flag),'rb')as f1:
        pro = pickle.load(f1)
    return pro


def DepoError(p,n):
    noise = depolarizing_error(p,n)
    return noise

r = 1
pm = 0.02
ped = 0.00001
pst = 0
MagError = DepoError(pm*r,1)
sQError = DepoError(pst*r,1)
sQError_s = SuperOp(sQError)
sQError_m = np.array(sQError_s)
tQError = DepoError(pst*r,2)
tQError_s = SuperOp(tQError)
tQError_m = np.array(tQError_s)
edError = DepoError(ped*r,1)
Twirl = SuperOp(Twirling(sQError_m))
Twirl_in = Twirl.to_instruction()

Tdg = QuantumCircuit(3)
Tdg.h(0)
Tdg.cx(0,2)
Tdg.h(1)
Tdg.t(1)
Tdg.append(MagError,[1])
Tdg.append(edError,[1])
Tdg.append(Twirl_in,[1])
Tdg.cx(1,0)
Tdg.append(tQError,[1,0])
Tdg.append(sQError,[0])
mat = np.array(DensityMatrix.from_instruction(Tdg))
identity = Operator(np.eye(2**3))

############投影为0态
projector = (Operator.from_label('IIZ')+identity)/2
projected_rho = projector @ mat @ projector
pPlus = np.trace(projected_rho)
projected_rho /= pPlus

projected_rho=DensityMatrix(projected_rho)

qc = QuantumCircuit(3)
qc.s(1)
qc.append(sQError,[1])
qc.z(1)
Choi1 = projected_rho.evolve(qc)


############投影为1态
projector = (-Operator.from_label('IIZ')+identity)/2
projected_rho = projector @ mat @ projector
pminu = np.trace(projected_rho)
projected_rho /= pminu

projected_rho=DensityMatrix(projected_rho)

qc = QuantumCircuit(3)
qc.x(1)
Choi2 = projected_rho.evolve(qc)

Choimat = DensityMatrix(pPlus*Choi1+pminu*Choi2)

# projected_rho = np.real_if_close(projected_rho, tol=tol)
Choimat = partial_trace(Choimat,[0])
Choimat = np.array(Choimat/np.trace(Choimat))
Choimat= Choimat*2

TdgError = Choi(Choimat).to_instruction()



statime= time.time()
# sigList0 = generate_valid_list()
# # 提取原列表的第 8、12、14、15 个元素 (索引从 0 开始)
# selected_elements = [sigList0[7], sigList0[3], sigList0[1], sigList0[0]]

# # 剩余的元素
# remaining_elements = [sigList0[i] for i in range(len(sigList0)) if i not in [7, 3, 1, 0]]

# # 翻转剩余的列表
# reversed_remaining = remaining_elements[::-1]

# # 合并结果
# sigList = selected_elements + remaining_elements
# sig = 0
import itertools

# 生成所有包含4个0或1的组合
all_combinations = list(itertools.product([0, 1], repeat=4))

# 将生成的组合转换为二维列表
Siglist = [list(combination) for combination in all_combinations]
rhoList0 = []
normList0 = []
#第一步--------------------------------------------------------------


qc = QuantumCircuit(8)
qc.h(0)
for i in range(8):
    qc.append(sQError,[i])
label = [1,2,3,4,5,6,7]
for i in range(len(label)):
    qc.cx(0,label[i])
    qc.append(tQError,[0,label[i]])
qc.append(TdgError,[0])
qc.append(sQError,[0])
matrix0 = DensityMatrix.from_instruction(qc)
projector = Mx1(8,0)
# sig = sig+1
projected_rho = projector @ matrix0 @ projector
norm = np.trace(projected_rho)
normList0.append(norm)
projected_rho /= norm
matrix = partial_trace(DensityMatrix(projected_rho),[0])
rhoList0.append(matrix)

projector = Mx1(8,1)
# sig = sig+1
projected_rho = projector @ matrix0 @ projector
norm = np.trace(projected_rho)
normList0.append(norm)
projected_rho /= norm
matrix = partial_trace(DensityMatrix(projected_rho),[0])
rhoList0.append(matrix)



#第二步--------------------------------------------------------------

# print(matpro)
qc = QuantumCircuit(11)
qc.h(10)
for i in range(4):
    qc.append(sQError,[10-i])
label = [0,1,2,3,7,8,9]
for i in range(len(label)):
    qc.cx(10,label[i])
    qc.append(tQError,[10,label[i]])
qc.append(TdgError,[10])
qc.append(sQError,[10])
qc0 = QuantumCircuit(4)
mat = DensityMatrix.from_instruction(qc0)
rhoList = []
normList = []
for i in range(len(rhoList0)):
    matrix = rhoList0[i]
    matpro = mat.tensor(matrix)
    matpro = matpro.evolve(qc)

    projector = Mx2(11,0)
    projected_rho = projector @ matpro  @ projector
    norm = np.trace(projected_rho)
    normList.append(norm*normList0[i])
    projected_rho /= norm
    matrix = partial_trace(DensityMatrix(projected_rho),[10])
    rhoList.append(matrix)

    projector = Mx2(11,1)
    projected_rho = projector @ matpro  @ projector
    norm = np.trace(projected_rho)
    normList.append(norm*normList0[i])
    projected_rho /= norm
    matrix = partial_trace(DensityMatrix(projected_rho),[10])
    rhoList.append(matrix)


# print(matrix)

#第三步--------------------------------------------------------------
# print(matpro)
qc = QuantumCircuit(12)
qc.h(11)
qc.append(sQError,[11])
qc.append(sQError,[10])
label = [10,8,7,5,4,1,0]
for i in range(len(label)):
    qc.cx(11,label[i])
    qc.append(tQError,[11,label[i]])
qc.append(TdgError,[11])
qc.append(sQError,[11])

qc0 = QuantumCircuit(2)
mat = DensityMatrix.from_instruction(qc0)
rhoList0 = []
normList0 = []
for i in range(len(rhoList)):
    matrix = rhoList[i]
    matpro = mat.tensor(matrix)


    matpro = matpro.evolve(qc)
    projector = Mx2(12,0)
    projected_rho = projector @ matpro  @ projector
    norm = np.trace(projected_rho)
    normList0.append(norm*normList[i])
    projected_rho /= norm
    matrix = partial_trace(DensityMatrix(projected_rho),[11])
    rhoList0.append(matrix)

    projector = Mx2(12,1)
    projected_rho = projector @ matpro  @ projector
    norm = np.trace(projected_rho)
    normList0.append(norm*normList[i])
    projected_rho /= norm
    matrix = partial_trace(DensityMatrix(projected_rho),[11])
    rhoList0.append(matrix)

#第四步--------------------------------------------------------------


qc = QuantumCircuit(12)
qc.h(11)
qc.append(sQError,[11])
label = [10,9,7,6,4,2,0]
for i in range(len(label)):
    qc.cx(11,label[i])
    qc.append(tQError,[11,label[i]])
qc.append(TdgError,[11])
qc.append(sQError,[11])

qc0 = QuantumCircuit(1)
mat = DensityMatrix.from_instruction(qc0)

rhoList = []
normList = []
for i in range(len(rhoList0)):
    matrix = rhoList0[i]
    matpro = mat.tensor(matrix)


    matpro = matpro.evolve(qc)
    projector = Mx2(12,0)
    projected_rho = projector @ matpro  @ projector
    norm = np.trace(projected_rho)
    normList.append(norm*normList0[i])
    projected_rho /= norm
    matrix = partial_trace(DensityMatrix(projected_rho),[11])
    rhoList.append(matrix)

    projector = Mx2(12,1)
    projected_rho = projector @ matpro  @ projector
    norm = np.trace(projected_rho)
    normList.append(norm*normList0[i])
    projected_rho /= norm
    matrix = partial_trace(DensityMatrix(projected_rho),[11])
    rhoList.append(matrix)
# print(matrix)

#第五步--------------------------------------------------------------

qc = QuantumCircuit(12)
qc.h(11)
qc.append(sQError,[11])
qc.cx(11,0)
qc.append(tQError,[11,0])

qc0 = QuantumCircuit(1)
mat = DensityMatrix.from_instruction(qc0)

rhoList0 = []
normList0 = []
for i in range(len(rhoList)):
    matrix = rhoList[i]
    matpro = mat.tensor(matrix)
    matpro = matpro.evolve(qc)
    rhoList[i] = matpro
# print(matrix)

#第六步--------------------------------------------------------------

qc = QuantumCircuit(12)
label = [3,5,6,8,9,10]
for i in range(len(label)):
    qc.cx(0,label[i])
    qc.append(tQError,[0,label[i]])
for i in range(len(rhoList)):
    matrix = rhoList[i]
    matpro = matrix.evolve(qc)
    rhoList[i] = matpro

# print(matrix)
#第七步--------------------------------------------------------------
z = Operator.from_label('ZIIIIIIIIIII')
qc = QuantumCircuit(12)
for i in range(11):
    qc.append(TdgError,[i])
    qc.append(sQError,[i])
    qc.cx(11,i)

    # qc.cx(11,i)

matrix = rhoList[0]
matrix = matrix.evolve(qc)
projector = Mx3(Siglist[0])
projected_rho = projector @ matrix @ projector
print(partial_trace(DensityMatrix(projected_rho/np.trace(projected_rho)),[0,1,2,3,4,5,6,7,8,9,10]))
rho = projected_rho*normList[0]
for i in range(len(rhoList)-1):

    matrix = rhoList[i+1]
    matrix = matrix.evolve(qc)
    projector = Mx3(Siglist[i+1])
    projected_rho = projector @ matrix @ projector
    if sum(Siglist[i+1])%2==1:
        print('Z')
        projected_rho = z@projected_rho@z
    print(partial_trace(DensityMatrix(projected_rho/np.trace(projected_rho)),[0,1,2,3,4,5,6,7,8,9,10]))
    rho = rho + projected_rho*normList[i+1]
    
prosuc = np.trace(rho)
rho /= prosuc
matrixF = partial_trace(DensityMatrix(rho),[0,1,2,3,4,5,6,7,8,9,10])
# Z = Operator.from_label('Z')
# if sum(sigList)%2 ==1:
#     matrixF=matrixF.evolve(Z)
print('提纯成功概率:',prosuc)
print(matrixF)




qc0 = QuantumCircuit(2)
mat = DensityMatrix.from_instruction(qc0)
rho = matrixF.tensor(mat)
qc = QuantumCircuit(3)
qc.h(0)
qc.append(sQError,[0])
qc.h(1)
qc.append(sQError,[1])
qc.append(Twirl_in,[2])
qc.cx(0,1)
qc.append(tQError,[0,1])
qc.cx(2,1)
qc.append(tQError,[2,1])
qc.append(sQError,[1])
rho = rho.evolve(qc)
identity = Operator(np.eye(2**3))
ch = 'IZI'

projector = (Operator.from_label(ch)+identity)/2
rho1 = projector @ rho @ projector
p1 = np.trace(rho1)
rho1 = partial_trace(DensityMatrix(rho1/p1),[1])
qc=QuantumCircuit(2)
qc.cx(0,1)
qc.append(tQError,[0,1])
qc.append(sQError,[0])
qc.append(sQError,[1])
rho1= rho1.evolve(qc)
# o1 = rho1.expectation_value(Operator.from_label('XX'))

projector = (-Operator.from_label(ch)+identity)/2
rho2 = projector @ rho @ projector
p2 = np.trace(rho2)
rho2 = partial_trace(DensityMatrix(rho2/p2),[1])
qc=QuantumCircuit(2)
qc.s(1)
qc.append(sQError,[1])
qc.x(1)
qc.z(1)
qc.cx(0,1)
qc.append(tQError,[0,1])
qc.append(sQError,[0])
qc.append(sQError,[1])
rho2= rho2.evolve(qc)
# o2 = rho2.expectation_value(Operator.from_label('XX'))

# o = p1*o1+p2*o2

endtime= time.time()
print('模拟时间：',endtime-statime)
# print('结果：',o)
Olist0 = ['XX','XI','IX','II']
Olist = [Operator.from_label(x)for x in Olist0]
Ovalue = []
for i in range(len(Olist)):
    o1 = rho1.expectation_value(Olist[i])
    o2 = rho2.expectation_value(Olist[i])
    o = p1*o1*prosuc+p2*o2*prosuc
    Ovalue.append(o)
import pickle
# with open('./Result/errorFree','wb') as f1:
#     pickle.dump(Ovalue,f1)
# with open('./Result/errorMagic','wb') as f1:
#     pickle.dump(Ovalue,f1)
# with open('./Result/errorAll','wb') as f1:
#     pickle.dump(Ovalue,f1)
# with open('./ResPEC2/Endecode/Raw_'+str(p),'wb') as f1:
#     pickle.dump(Ovalue,f1)
# with open('./ResPEC2/Stabilizer/Raw_'+str(p),'wb') as f1:
#     pickle.dump(Ovalue,f1)
with open('./ResPEC2/Allerror/Raw_'+str(r),'wb') as f1:
    pickle.dump(Ovalue,f1)
# with open('./ResPEC2/Magic/Raw_'+str(p),'wb') as f1:
#     pickle.dump(Ovalue,f1)
print(Ovalue)
