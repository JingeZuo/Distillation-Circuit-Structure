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
def XInvevolution(A):
    C=[15,1,2,4,8,16]
    T=[3,5,6,7,9,10,11,12,13,14,15]
    CX=[[3,5,6,9,10,12],
        [3,5,7,9,11,13,15],
        [3,6,7,10,11,14,15],
        [5,6,7,12,13,14,15],
        [9,10,11,12,13,14,15],
        [15]]
    EV=A.copy()
    for i in range(6):
        B=EV[:,-1,np.newaxis].copy()
        for j in range(len(CX[i])):
            B[CX[i][j]-1][0]=(B[CX[i][j]-1][0]+B[C[i]-1][0])%2
        EV = np.hstack((EV, B))
    return EV
A=np.array([[1],[0],[1],[0],[1],[0],[1],[0],[1],[0],[1],[0],[1],[0],[1],[0]])

def ZInvevolution(A):
    C=[15,1,2,4,8,16]
    T=[3,5,6,7,9,10,11,12,13,14,15]
    CX=[[3,5,6,9,10,12],
        [3,5,7,9,11,13,15],
        [3,6,7,10,11,14,15],
        [5,6,7,12,13,14,15],
        [9,10,11,12,13,14,15],
        [15]]
    EV=A.copy()
    for i in range(6):
        s=0
        for j in range(len(CX[i])):
            s = s + EV[CX[i][j]-1][i]
        B=EV[:,-1,np.newaxis].copy()
        B[C[i]-1][0]=(B[C[i]-1][0]+s)%2
        EV=np.hstack((EV,B))
    return EV
A=np.array([[1],[0],[1],[0],[1],[0],[1],[0],[1],[0],[1],[0],[1],[0],[1],[0]])
XEV=XInvevolution(A)

ZEV=ZInvevolution(A)
Z=np.array(generate_binary_combinations(A))
bra=[]

for i in range(len(generate_binary_combinations(A))):
    S=np.array(ZInvevolution(Z[i]))
    bra.append(np.vstack((XEV, S)))
bra=np.array(bra)
print(bra.shape)
