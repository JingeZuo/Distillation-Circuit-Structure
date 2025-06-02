import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from sympy import div, Poly
from sympy.polys.domains import ZZ
from sympy import Matrix, eye, zeros,degree
from scipy.linalg import null_space
from sympy import symbols, factor
import galois
import qiskit
from qiskit.quantum_info import Statevector,Operator
def mod2(matrix):
    """Reduce a matrix to modulo 2"""
    return np.mod(matrix, 2)
def nullspace(matrix):
    # 将 H 转换为 GF(2) 类型
    GF = galois.GF(2)
    H_gf = GF(matrix)

    # 求 H 的零空间（null space），结果是 G 的行空间
    G_gf = H_gf.null_space()

    # 转换为 numpy 数组或直接使用
    G = G_gf.view(np.ndarray).astype(int)
    return G
def fact(poly):
    # 定义变量
    x = symbols('x')
    # 因式分解
    factored_poly = factor(poly)
    return factored_poly
def polynomial_to_circulant(poly, l):
    x = symbols('x')

    if not isinstance(poly, Poly):
        poly = Poly(poly, x, domain=ZZ)

    coeffs = poly.all_coeffs()

    # 系数需要从低次幂到高次幂排列
    coeffs.reverse()

    # Create a l \times l matrix
    circulant_matrix = np.zeros((l, l), dtype=int)

    # Fill the elements to get the circulant of  the "poly"
    for i in range(l):
        a1 = np.pad(coeffs, (0, l - len(coeffs)), 'constant')
        circulant_matrix[i] = row = np.roll(a1, i)

    return circulant_matrix
def distance(G):
    G=np.array(G)
    minvalue=[]
    for i in range(len(G)):
        n=0
        for j in range(len(G[i])):
            if G[i][j] != 0:
                n=n+1
        minvalue.append(n)
    return min(minvalue)
e=np.array([[1,0],[0,1]])
pauliX=np.array([[0,1],[1,0]])
#%%
n=4
a4=np.array([[1,1],[0,1]])
b4=np.array([[0,0],[1,0]])
H14=np.kron(e,a4)+np.kron(pauliX,b4)
H2p4=np.kron(a4,e)+np.kron(b4,pauliX)
r14=len(H14)
n14=len(H14[0])
r24=len(H2p4)
n24=len(H2p4[0])
E14=np.eye(int(r14/2))
E14t=np.eye(int(n14/2))
E24=np.eye(int(r24/2))
E24t=np.eye(int(n24/2))
GX4=np.hstack((np.kron(E24,H14),np.kron(H2p4,E14)))
GZ4=np.hstack((np.kron(H2p4.T,E14t),np.kron(E24t,H14.T)))
print(len(GX4),len(GZ4))
print(np.linalg.matrix_rank(GX4),np.linalg.matrix_rank(GZ4))
print(GX4)
print(GZ4)
#%%
N=8
a8=np.array([[1,1,0,0],[0,1,1,0],[0,0,1,1],[0,0,0,1]])
b8=np.array([[0,0,0,0],[0,0,0,0],[0,0,0,0],[1,0,0,0]])
H18=np.kron(e,a8)+np.kron(pauliX,b8)
H2p8=np.kron(a8,e)+np.kron(b8,pauliX)
r18=len(H18)
n18=len(H18[0])
r28=len(H2p8)
n28=len(H2p8[0])
E18=np.eye(int(r18/2))
E18t=np.eye(int(n18/2))
E28=np.eye(int(r28/2))
E28t=np.eye(int(n28/2))
GX8=np.hstack((np.kron(E28,H18),np.kron(H2p8,E18)))
GZ8=np.hstack((np.kron(H2p8.T,E18t),np.kron(E28t,H18.T)))
print(len(GX8),len(GZ8))
print(np.linalg.matrix_rank(GX8),np.linalg.matrix_rank(GZ8))

#%%
qc=QuantumCircuit(16)
qc.h(15)

for i in [14,7,3]:
    qc.cx(15,i)
qc.h(14)
for i in [12,6,2]:
    qc.cx(14,i)
state=Statevector.from_instruction(qc)
qc=QuantumCircuit(16)
qc.x([14,6,2])
stateproject=(state+state.evolve(qc))/2
print(np.linalg.norm(stateproject))