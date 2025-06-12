import qiskit
from matplotlib import pyplot as plt
from qiskit import QuantumCircuit, transpile
from qiskit.circuit.library import XGate
from qiskit.quantum_info import Clifford, Statevector, DensityMatrix
from qiskit_aer import AerSimulator
import numpy as np
from scipy.linalg import block_diag
from qiskit.quantum_info import SuperOp,Statevector,Pauli,DensityMatrix,Operator,partial_trace,Clifford,PTM,Choi
def inver(A,q):
    B=[]
    for i in range(len(A)):
        B.append(len(q)-A[i]+1)
    return B
def sur(a):
    s=[]
    if a-4>0:
        s.append(a-4)
    if a%9!=5:
        s.append(a)
    if a%9!=0:
        s.append(a +1)
    if a+5<=41:
        s.append(a + 5)
    return s
def p9(a,k):
    s=[]
    for i in range(len(a)):
        s.append(a[i]+9*k)
    return s
def rowdistance(A):
    n=0
    for i in range(len(A)):
        if A[i]!=0:
            n=n+1
    return n
def move_column(matrix, i, j):
    """
    将矩阵的第 i 列前移到第 j 列前面
    :param matrix: numpy 二维数组
    :param i: 原始列号（要移动的列）
    :param j: 目标位置（插入到该列前）
    :return: 新矩阵
    """
    if i < 0 or i >= matrix.shape[1] or j < 0 or j > matrix.shape[1]:
        raise ValueError("索引超出范围")

    col_to_move = matrix[:, i]                 # 提取第 i 列
    matrix = np.delete(matrix, i, axis=1)     # 删除原列
    matrix = np.insert(matrix, j, col_to_move, axis=1)  # 插入到 j 列前
    return matrix
def move_row(matrix, i, j):
    """
    将矩阵的第 i 行前移到第 j 位置前面
    :param matrix: numpy 二维数组
    :param i: 原始行号（要移动的行）
    :param j: 目标位置（插入到该位置前）
    :return: 新矩阵
    """
    if i < 0 or i >= matrix.shape[0] or j < 0 or j > matrix.shape[0]:
        raise ValueError("索引超出范围")

    # 删除第 i 行，并将其插入到 j 位置前
    row_to_move = matrix[i]
    matrix = np.delete(matrix, i, axis=0)
    matrix = np.insert(matrix, j, row_to_move, axis=0)
    return matrix
genX=[]
genZ=[]
HX=[]
HZ=[]
for i in range(20):
    HX.append(np.zeros(1*41).tolist())
    HZ.append(np.zeros(1*41).tolist())
n=0
for i in range(5):
    for j in p9([1,2,3,4],i):
        genX.append(sur(j))
        for k in sur(j):
            HX[n][k-1]=1
        n=n+1
n=0

for i in range(4):
    for j in p9([5,6,7,8,9],i):
        genZ.append(sur(j))
        for k in sur(j):
            HZ[n][k-1]=1
        n=n+1

HX=np.array(HX)
HZ=np.array(HZ)
LogicalX=np.zeros((1,41))
LogicalZ=np.zeros((1,41))
for i in [0,1,2,3,4]:
    LogicalX[0][i]=1
for i in [0,9,18,27,36]:
    LogicalZ[0][i]=1
H15X=HX
H15Z=np.vstack((HZ,LogicalZ))
H16X=np.vstack((HX,LogicalX))
H16Z=HZ
MHX=block_diag(H15X,H16X)
MHZ=block_diag(H15Z,H16Z)

for i in range(14,0,-1):
    if i in [1,2,4,8]:
        MHX=block_diag([1],MHX)
        MHZ=block_diag([0],MHZ)
    else:
        MHX=block_diag([0],MHX)
        MHZ=block_diag([1],MHZ)
for i in range(11):
    MHX=block_diag(MHX,[1])
    MHZ=block_diag(MHZ,[0])
MEHX=[]
MEHZ=[]
for i in range(len(MHX)):
    if all(x==0 for x in MHX[i]):
        MEHX.append(i)
for i in range(len(MHZ)):
    if all(x==0 for x in MHZ[i]):
        MEHZ.append(i)
for i in MEHX[::-1]:
    MHX=np.delete(MHX,i,axis=0)
for i in MEHZ[::-1]:
    MHZ=np.delete(MHZ,i,axis=0)
s=[]
for i in range(len(MHZ)):
    if rowdistance(MHZ[i]) != 1:
        s.append(i)

MEHX=MHX.copy()
MEHZ=MHZ.copy()
for i in s[:5]:
    MHX=move_column(MHX,i,0)
    MHZ=move_column(MHZ,i,0)
for i in range(5):
    MHX = move_column(MHX, 4, i)
    MHZ = move_column(MHZ, 4, i)

MEHX=MHX.copy()
MEHZ=MHZ.copy()
for i in [97,98,99,100,101]:
    MHX=move_column(MHX,i-1,5)
    MHZ=move_column(MHZ,i-1,5)
for i in range(5):
    MHX = move_column(MHX, 9, i+5)
    MHZ = move_column(MHZ, 9, i+5)
testX=MHX[:,:10]
testZ=MHZ[:,:10]
sX=[]
sZ=[]
for i in range(len(testX)):
    if rowdistance(testX[i]) !=0:
        sX.append(i)
for i in range(len(testZ)):
    if rowdistance(testZ[i]) !=0:
        sZ.append(i)
MEHX=MHX.copy()
MEHZ=MHZ.copy()
for i in sX:
    MHX=move_row(MHX,i,0)
for i in sZ:
    MHZ=move_row(MHZ,i,0)
for i in range(6):
    MHX = move_row(MHX, 5, i)
    MHZ = move_row(MHZ, 5, i)
#%%
from reportlab.lib.pagesizes import A4, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Spacer
from reportlab.lib import colors
import numpy as np

# 示例数据：一个较宽的矩阵（例如 10 列）
data = MHX
# 转换为 Python 原生列表，并转为字符串格式
matrix = [[str(cell) for cell in row] for row in data.tolist()]

# 可选：添加表头
headers = ["列{}".format(i+1) for i in range(data.shape[1])]
matrix = [headers] + matrix

# 设置页面为横向 A4
pdf_file = "wide_matrix_landscape.pdf"
page_size = landscape(A4)  # <<<<<<<<<<<<< 横向页面设置

# 创
# 建PDF文档
doc = SimpleDocTemplate(pdf_file, pagesize=page_size,
                        leftMargin=20, rightMargin=20,
                        topMargin=20, bottomMargin=20)
elements = []

# 创建表格
table = Table(matrix)

# 设置表格样式
style = TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTSIZE', (0, 0), (-1, 0), 12),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ('FONTSIZE', (0, 1), (-1, -1), 10),
])
table.setStyle(style)

# 自动调整每列宽度以适应页面
available_width = page_size[0] - doc.leftMargin - doc.rightMargin
col_width = available_width / len(matrix[0])
table._argW = [col_width] * len(matrix[0])  # 每列等宽

# 添加表格到文档
elements.append(table)
doc.build(elements)

print(f"✅ 已生成 PDF 文件（横向页面）：{pdf_file}")


