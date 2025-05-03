import numpy as np
import itertools
def generate_binary_combinations(input_matrix):
    # 输入矩阵应为m*1的numpy数组或列表
    m = len(input_matrix)  # 获取输入矩阵的行数m
    ones_indices = [i for i, val in enumerate(input_matrix) if val == 1]
    n = len(ones_indices)
    all_combinations = []

    # 生成1到n个元素的组合
    for k in range(0, n + 1):
        for combo in itertools.combinations(ones_indices, k):
            matrix = np.zeros((m, 1), dtype=int)  # 动态创建m*1的零矩阵
            matrix[list(combo), 0] = 1  # 明确指定列索引为0
            all_combinations.append(matrix)

    return all_combinations
def Xevolution(C,CX,A):
    EV=A.copy()
    for i in range(len(C)):
        B=EV[:,-1,np.newaxis].copy()
        for j in range(len(CX[i])):
            B[CX[i][j]-1][0]=(B[CX[i][j]-1][0]+B[C[i]-1][0])%2
        EV = np.hstack((EV, B))
    return EV


def Zevolution(C,CX,A):
    EV=A.copy()
    for i in range(len(C)):
        s=0
        for j in range(len(CX[i])):
            s = s + EV[CX[i][j]-1][i]
        B=EV[:,-1,np.newaxis].copy()
        B[C[i]-1][0]=(B[C[i]-1][0]+s)%2
        EV=np.hstack((EV,B))
    return EV

C=[15,1,2,4,8,16]
CX=[[3,5,6,9,10,12],
        [3,5,7,9,11,13,15],
        [3,6,7,10,11,14,15],
        [5,6,7,12,13,14,15],
        [9,10,11,12,13,14,15],
        [15]]

g1=np.array([[1],[0],[1],[0],[1],[0],[1],[0],[1],[0],[1],[0],[1],[0],[1],[0]])
g1XEV=Xevolution(C,CX,g1)
g1ZEV=Zevolution(C,CX,g1)
g1Z=np.array(generate_binary_combinations(g1))
G1=[]
for i in range(len(generate_binary_combinations(g1))):
    S=np.array(Zevolution(C,CX,g1Z[i]))
    G1.append(np.vstack((g1XEV, S)))
G1=np.array(G1)

g2=np.array([[0],[1],[1],[0],[0],[1],[1],[0],[0],[1],[1],[0],[0],[1],[1],[0]])
g2XEV=Xevolution(C,CX,g2)
g2ZEV=Zevolution(C,CX,g2)
g2Z=np.array(generate_binary_combinations(g2))
G2=[]
for i in range(len(generate_binary_combinations(g2))):
    S=np.array(Zevolution(C,CX,g2Z[i]))
    G2.append(np.vstack((g2XEV, S)))
G2=np.array(G2)

g3=np.array([[0],[0],[0],[1],[1],[1],[1],[0],[0],[0],[0],[1],[1],[1],[1],[0]])
g3XEV=Xevolution(C,CX,g3)
g3ZEV=Zevolution(C,CX,g3)
g3Z=np.array(generate_binary_combinations(g3))
G3=[]
for i in range(len(generate_binary_combinations(g3))):
    S=np.array(Zevolution(C,CX,g3Z[i]))
    G3.append(np.vstack((g3XEV, S)))
G3=np.array(G3)

g4=np.array([[0],[0],[0],[0],[0],[0],[0],[1],[1],[1],[1],[1],[1],[1],[1],[0]])
g4XEV=Xevolution(C,CX,g4)
g4ZEV=Zevolution(C,CX,g4)
g4Z=np.array(generate_binary_combinations(g4))
G4=[]
for i in range(len(generate_binary_combinations(g4))):
    S=np.array(Zevolution(C,CX,g4Z[i]))
    G4.append(np.vstack((g4XEV, S)))
G4=np.array(G4)
print(G1.shape,G2.shape,G3.shape,G4.shape)
