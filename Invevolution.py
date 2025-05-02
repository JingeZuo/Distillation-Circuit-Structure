import numpy as np
import matplotlib.pyplot as plt
#%%
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
print(XInvevolution(A))
#%%
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
A=np.array([[0],[1],[1],[0],[0],[1],[1],[0],[0],[1],[1],[0],[0],[1],[1],[0]])
print(ZInvevolution(A))




