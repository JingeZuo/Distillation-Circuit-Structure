import dash
import dash_cytoscape as cyto
from dash import html
#%%
TGpri = dash.Dash(__name__)
elements = [
#第1列
{'data': {'id': 'q1', 'label': '+1','group': 'q'}, 'position': {'x': 0, 'y': 0}},
{'data': {'id': 'q2', 'label': '+2','group': 'q'}, 'position': {'x': 0, 'y': 100}},
{'data': {'id': 'q3', 'label': '+3','group': 'q'}, 'position': {'x': 0, 'y': 200}},
{'data': {'id': 'q4', 'label': '+4','group': 'q'}, 'position': {'x': 0, 'y': 300}},
{'data': {'id': 'q5', 'label': '+5','group': 'q'}, 'position': {'x': 0, 'y': 400}},
{'data': {'id': 'q6', 'label': '+6','group': 'q'}, 'position': {'x': 0, 'y': 500}},
{'data': {'id': 'q7', 'label': '+7','group': 'q'}, 'position': {'x': 0, 'y': 600}},
{'data': {'id': 'q8', 'label': '+8','group': 'q'}, 'position': {'x': 0, 'y': 700}},
{'data': {'id': 'q9', 'label': '+9','group': 'q'}, 'position': {'x': 0, 'y': 800}},
{'data': {'id': 'q10', 'label': '+10','group': 'q'}, 'position': {'x': 0, 'y': 900}},
{'data': {'id': 'q11', 'label': '+11','group': 'q'}, 'position': {'x': 0, 'y': 1000}},
{'data': {'id': 'q12', 'label': '+12','group': 'q'}, 'position': {'x': 0, 'y': 1100}},
{'data': {'id': 'q13', 'label': '+13','group': 'q'}, 'position': {'x': 0, 'y': 1200}},
{'data': {'id': 'q14', 'label': '+14','group': 'q'}, 'position': {'x': 0, 'y': 1300}},
{'data': {'id': 'q15', 'label': '+15','group': 'q'}, 'position': {'x': 0, 'y': 1400}},
{'data': {'id': 'q16', 'label': '+16','group': 'q'}, 'position': {'x': 0, 'y': 1500}},
#第2列
{'data': {'id': 'T1', 'label': 'T','group': 'O'}, 'position': {'x': 100, 'y': 100}},
{'data': {'id': 'T2', 'label': 'T','group': 'O'}, 'position': {'x': 100, 'y': 200}},
{'data': {'id': 'T3', 'label': 'T','group': 'O'}, 'position': {'x': 100, 'y': 300}},
{'data': {'id': 'T4', 'label': 'T','group': 'O'}, 'position': {'x': 100, 'y': 400}},
{'data': {'id': 'E21', 'group': 'E'}, 'position': {'x': 50, 'y': 100}},
{'data': {'id': 'E31', 'group': 'E'}, 'position': {'x': 50, 'y': 200}},
{'data': {'id': 'E41', 'group': 'E'}, 'position': {'x': 50, 'y': 300}},
{'data': {'id': 'E51', 'group': 'E'}, 'position': {'x': 50, 'y': 400}},
{'data': {'id': 'E22', 'group': 'E'}, 'position': {'x': 150, 'y': 100}},
{'data': {'id': 'E32', 'group': 'E'}, 'position': {'x': 150, 'y': 200}},
{'data': {'id': 'E42', 'group': 'E'}, 'position': {'x': 150, 'y': 300}},
{'data': {'id': 'E52', 'group': 'E'}, 'position': {'x': 150, 'y': 400}},
#第3列
{'data': {'id': 'Z5', 'label': 'Z2\nZ3\nZ4\nZ6','group': 'MO'}, 'position': {'x': 200, 'y': 750}},
{'data': {'id': 'Z5.', 'group': 'p'}, 'position': {'x': 300, 'y': 750}},
{'data': {'id': 'Z5X', 'label': 'X','group': 'O'}, 'position': {'x': 300, 'y': 500}},
{'data': {'source': 'Z5', 'target': 'Z5.'}},
{'data': {'source': 'Z5X', 'target': 'Z5.'}},
#第4列
{'data': {'id': 'Z6', 'label': 'Z1\nZ2\nZ3\nZ7','group': 'MO'}, 'position': {'x': 400, 'y': 750}},
{'data': {'id': 'Z6.', 'group': 'p'}, 'position': {'x': 500, 'y': 750}},
{'data': {'id': 'Z6X', 'label': 'X','group': 'O'}, 'position': {'x': 500, 'y': 600}},
{'data': {'source': 'Z6', 'target': 'Z6.'}},
{'data': {'source': 'Z6X', 'target': 'Z6.'}},
#第5列
{'data': {'id': 'Z7', 'label': 'Z1\nZ2\nZ4\nZ8','group': 'MO'}, 'position': {'x': 600, 'y': 750}},
{'data': {'id': 'Z7.', 'group': 'p'}, 'position': {'x': 700, 'y': 750}},
{'data': {'id': 'Z7X', 'label': 'X','group': 'O'}, 'position': {'x': 700, 'y': 700}},
{'data': {'source': 'Z7', 'target': 'Z7.'}},
{'data': {'source': 'Z7X', 'target': 'Z7.'}},
#第6列
{'data': {'id': 'Z8', 'label': 'Z1\nZ3\nZ4\nZ9','group': 'MO'}, 'position': {'x': 800, 'y': 750}},
{'data': {'id': 'Z8.', 'group': 'p'}, 'position': {'x': 900, 'y': 750}},
{'data': {'id': 'Z8X', 'label': 'X','group': 'O'}, 'position': {'x': 900, 'y': 800}},
{'data': {'source': 'Z8', 'target': 'Z8.'}},
{'data': {'source': 'Z8X', 'target': 'Z8.'}},
#第7列
{'data': {'id': 'Z9', 'label': 'Z1\nZ4\nZ5\nZ10','group': 'MO'}, 'position': {'x': 1000, 'y': 750}},
{'data': {'id': 'Z9.', 'group': 'p'}, 'position': {'x': 1100, 'y': 750}},
{'data': {'id': 'Z9X', 'label': 'X','group': 'O'}, 'position': {'x': 1100, 'y': 900}},
{'data': {'source': 'Z9', 'target': 'Z9.'}},
{'data': {'source': 'Z9X', 'target': 'Z9.'}},
#第8列
{'data': {'id': 'Z10', 'label': 'Z1\nZ2\nZ5\nZ11','group': 'MO'}, 'position': {'x': 1200, 'y': 750}},
{'data': {'id': 'Z10.', 'group': 'p'}, 'position': {'x': 1300, 'y': 750}},
{'data': {'id': 'Z10X', 'label': 'X','group': 'O'}, 'position': {'x': 1300, 'y': 1000}},
{'data': {'source': 'Z10', 'target': 'Z10.'}},
{'data': {'source': 'Z10X', 'target': 'Z10.'}},
#第9列
{'data': {'id': 'Z11', 'label': 'Z1\nZ3\nZ5\nZ12','group': 'MO'}, 'position': {'x': 1400, 'y': 750}},
{'data': {'id': 'Z11.', 'group': 'p'}, 'position': {'x': 1500, 'y': 750}},
{'data': {'id': 'Z11X', 'label': 'X','group': 'O'}, 'position': {'x': 1500, 'y': 1100}},
{'data': {'source': 'Z11', 'target': 'Z11.'}},
{'data': {'source': 'Z11X', 'target': 'Z11.'}},
#第10列
{'data': {'id': 'Z12', 'label': 'Z1\nZ2\nZ3\nZ4\nZ5\nZ13','group': 'MO'}, 'position': {'x': 1600, 'y': 750}},
{'data': {'id': 'Z12.', 'group': 'p'}, 'position': {'x': 1700, 'y': 750}},
{'data': {'id': 'Z12X', 'label': 'X','group': 'O'}, 'position': {'x': 1700, 'y': 1200}},
{'data': {'source': 'Z12', 'target': 'Z12.'}},
{'data': {'source': 'Z12X', 'target': 'Z12.'}},
#第11列
{'data': {'id': 'Z13', 'label': 'Z3\nZ4\nZ5\nZ14','group': 'MO'}, 'position': {'x': 1800, 'y': 750}},
{'data': {'id': 'Z13.', 'group': 'p'}, 'position': {'x': 1900, 'y': 750}},
{'data': {'id': 'Z13X', 'label': 'X','group': 'O'}, 'position': {'x': 1900, 'y': 1300}},
{'data': {'source': 'Z13', 'target': 'Z13.'}},
{'data': {'source': 'Z13X', 'target': 'Z13.'}},
#第12列
{'data': {'id': 'Z14', 'label': 'Z2\nZ4\nZ5\nZ15','group': 'MO'}, 'position': {'x': 2000, 'y': 750}},
{'data': {'id': 'Z14.', 'group': 'p'}, 'position': {'x': 2100, 'y': 750}},
{'data': {'id': 'Z14X', 'label': 'X','group': 'O'}, 'position': {'x': 2100, 'y': 1400}},
{'data': {'source': 'Z14', 'target': 'Z14.'}},
{'data': {'source': 'Z14X', 'target': 'Z14.'}},
#第13列
{'data': {'id': 'Z15', 'label': 'Z2\nZ3\nZ5\nZ16','group': 'MO'}, 'position': {'x': 2200, 'y': 750}},
{'data': {'id': 'Z15.', 'group': 'p'}, 'position': {'x': 2300, 'y': 750}},
{'data': {'id': 'Z15X', 'label': 'X','group': 'O'}, 'position': {'x': 2300, 'y': 1500}},
{'data': {'source': 'Z15', 'target': 'Z15.'}},
{'data': {'source': 'Z15X', 'target': 'Z15.'}},
#第14列
{'data': {'id': 'T6', 'label': 'T','group': 'O'}, 'position': {'x': 2400, 'y': 500}},
{'data': {'id': 'T7', 'label': 'T','group': 'O'}, 'position': {'x': 2400, 'y': 600}},
{'data': {'id': 'T8', 'label': 'T','group': 'O'}, 'position': {'x': 2400, 'y': 700}},
{'data': {'id': 'T9', 'label': 'T','group': 'O'}, 'position': {'x': 2400, 'y': 800}},
{'data': {'id': 'T10', 'label': 'T','group': 'O'}, 'position': {'x': 2400, 'y': 900}},
{'data': {'id': 'T11', 'label': 'T','group': 'O'}, 'position': {'x': 2400, 'y': 1000}},
{'data': {'id': 'T12', 'label': 'T','group': 'O'}, 'position': {'x': 2400, 'y': 1100}},
{'data': {'id': 'T13', 'label': 'T','group': 'O'}, 'position': {'x': 2400, 'y': 1200}},
{'data': {'id': 'T14', 'label': 'T','group': 'O'}, 'position': {'x': 2400, 'y': 1300}},
{'data': {'id': 'T15', 'label': 'T','group': 'O'}, 'position': {'x': 2400, 'y': 1400}},
{'data': {'id': 'T16', 'label': 'T','group': 'O'}, 'position': {'x': 2400, 'y': 1500}},
{'data': {'id': 'E61', 'group': 'E'}, 'position': {'x': 2350, 'y': 500}},
{'data': {'id': 'E71', 'group': 'E'}, 'position': {'x': 2350, 'y': 600}},
{'data': {'id': 'E81', 'group': 'E'}, 'position': {'x': 2350, 'y': 700}},
{'data': {'id': 'E91', 'group': 'E'}, 'position': {'x': 2350, 'y': 800}},
{'data': {'id': 'E101', 'group': 'E'}, 'position': {'x': 2350, 'y': 900}},
{'data': {'id': 'E111', 'group': 'E'}, 'position': {'x': 2350, 'y': 1000}},
{'data': {'id': 'E121', 'group': 'E'}, 'position': {'x': 2350, 'y': 1100}},
{'data': {'id': 'E131', 'group': 'E'}, 'position': {'x': 2350, 'y': 1200}},
{'data': {'id': 'E141', 'group': 'E'}, 'position': {'x': 2350, 'y': 1300}},
{'data': {'id': 'E151', 'group': 'E'}, 'position': {'x': 2350, 'y': 1400}},
{'data': {'id': 'E161', 'group': 'E'}, 'position': {'x': 2350, 'y': 1500}},
{'data': {'id': 'E62', 'group': 'E'}, 'position': {'x': 2450, 'y': 500}},
{'data': {'id': 'E72', 'group': 'E'}, 'position': {'x': 2450, 'y': 600}},
{'data': {'id': 'E82', 'group': 'E'}, 'position': {'x': 2450, 'y': 700}},
{'data': {'id': 'E92', 'group': 'E'}, 'position': {'x': 2450, 'y': 800}},
{'data': {'id': 'E102', 'group': 'E'}, 'position': {'x': 2450, 'y': 900}},
{'data': {'id': 'E112', 'group': 'E'}, 'position': {'x': 2450, 'y': 1000}},
{'data': {'id': 'E122', 'group': 'E'}, 'position': {'x': 2450, 'y': 1100}},
{'data': {'id': 'E132', 'group': 'E'}, 'position': {'x': 2450, 'y': 1200}},
{'data': {'id': 'E142', 'group': 'E'}, 'position': {'x': 2450, 'y': 1300}},
{'data': {'id': 'E152', 'group': 'E'}, 'position': {'x': 2450, 'y': 1400}},
{'data': {'id': 'E162', 'group': 'E'}, 'position': {'x': 2450, 'y': 1500}},
#第15列
{'data': {'id': 'X6', 'label': 'X','group': 'O'}, 'position': {'x': 2500, 'y': 500}},
{'data': {'id': 'C6', 'label': 'Z2\nZ3\nZ4','group': 'CO'}, 'position': {'x': 2500, 'y': 200}},
{'data': {'source': 'X6', 'target': 'C6'}},
#第16列
{'data': {'id': 'X7', 'label': 'X','group': 'O'}, 'position': {'x': 2600, 'y': 600}},
{'data': {'id': 'C7', 'label': 'Z1\nZ2\nZ3','group': 'CO'}, 'position': {'x': 2600, 'y': 200}},
{'data': {'source': 'X7', 'target': 'C7'}},
#第17列
{'data': {'id': 'X8', 'label': 'X','group': 'O'}, 'position': {'x': 2700, 'y': 700}},
{'data': {'id': 'C8', 'label': 'Z1\nZ2\nZ4','group': 'CO'}, 'position': {'x': 2700, 'y': 200}},
{'data': {'source': 'X8', 'target': 'C8'}},
#第18列
{'data': {'id': 'X9', 'label': 'X','group': 'O'}, 'position': {'x': 2800, 'y': 800}},
{'data': {'id': 'C9', 'label': 'Z1\nZ3\nZ4','group': 'CO'}, 'position': {'x': 2800, 'y': 200}},
{'data': {'source': 'X9', 'target': 'C9'}},
#第19列
{'data': {'id': 'X10', 'label': 'X','group': 'O'}, 'position': {'x': 2900, 'y': 900}},
{'data': {'id': 'C10', 'label': 'Z1\nZ4\nZ5','group': 'CO'}, 'position': {'x': 2900, 'y': 200}},
{'data': {'source': 'X10', 'target': 'C10'}},
#第20列
{'data': {'id': 'X11', 'label': 'X','group': 'O'}, 'position': {'x': 3000, 'y': 1000}},
{'data': {'id': 'C11', 'label': 'Z1\nZ2\nZ5','group': 'CO'}, 'position': {'x': 3000, 'y': 200}},
{'data': {'source': 'X11', 'target': 'C11'}},
#第21列
{'data': {'id': 'X12', 'label': 'X','group': 'O'}, 'position': {'x': 3100, 'y': 1100}},
{'data': {'id': 'C12', 'label': 'Z1\nZ3\nZ5','group': 'CO'}, 'position': {'x': 3100, 'y': 200}},
{'data': {'source': 'X12', 'target': 'C12'}},
#第22列
{'data': {'id': 'X13', 'label': 'X','group': 'O'}, 'position': {'x': 3200, 'y': 1200}},
{'data': {'id': 'C13', 'label': 'Z1\nZ2\nZ3\nZ4\nZ5','group': 'CO'}, 'position': {'x': 3200, 'y': 200}},
{'data': {'source': 'X13', 'target': 'C13'}},
#第23列
{'data': {'id': 'X14', 'label': 'X','group': 'O'}, 'position': {'x': 3300, 'y': 1300}},
{'data': {'id': 'C14', 'label': 'Z3\nZ4\nZ5','group': 'CO'}, 'position': {'x': 3300, 'y': 200}},
{'data': {'source': 'X14', 'target': 'C14'}},
#第24列
{'data': {'id': 'X15', 'label': 'X','group': 'O'}, 'position': {'x': 3400, 'y': 1400}},
{'data': {'id': 'C15', 'label': 'Z2\nZ4\nZ5','group': 'CO'}, 'position': {'x': 3400, 'y': 200}},
{'data': {'source': 'X15', 'target': 'C15'}},
#第25列
{'data': {'id': 'X16', 'label': 'X','group': 'O'}, 'position': {'x': 3500, 'y': 1500}},
{'data': {'id': 'C16', 'label': 'Z2\nZ3\nZ5','group': 'CO'}, 'position': {'x': 3500, 'y': 200}},
{'data': {'source': 'X16', 'target': 'C16'}},
#第26列
{'data': {'id': 'X2', 'label': 'X','group': 'O'}, 'position': {'x': 3600, 'y': 100}},
{'data': {'id': 'X3', 'label': 'X','group': 'O'}, 'position': {'x': 3600, 'y': 200}},
{'data': {'id': 'X4', 'label': 'X','group': 'O'}, 'position': {'x': 3600, 'y': 300}},
{'data': {'id': 'X5', 'label': 'X','group': 'O'}, 'position': {'x': 3600, 'y': 400}},

#第16列
{'data': {'id': 'e1', 'group': 'q'}, 'position': {'x': 4000, 'y': 0}},

{'data': {'source': 'q1', 'target': 'e1'}},
{'data': {'source': 'q2', 'target': 'X2'}},
{'data': {'source': 'q3', 'target': 'X3'}},
{'data': {'source': 'q4', 'target': 'X4'}},
{'data': {'source': 'q5', 'target': 'X5'}},
{'data': {'source': 'q6', 'target': 'X6'}},
{'data': {'source': 'q7', 'target': 'X7'}},
{'data': {'source': 'q8', 'target': 'X8'}},
{'data': {'source': 'q9', 'target': 'X9'}},
{'data': {'source': 'q10', 'target': 'X10'}},
{'data': {'source': 'q11', 'target': 'X11'}},
{'data': {'source': 'q12', 'target': 'X12'}},
{'data': {'source': 'q13', 'target': 'X13'}},
{'data': {'source': 'q14', 'target': 'X14'}},
{'data': {'source': 'q15', 'target': 'X15'}},
{'data': {'source': 'q16', 'target': 'X16'}},

]
TGpri.layout = html.Div([
    cyto.Cytoscape(
        id='cytoscape-mixed',
        layout={'name': 'preset'},
        elements=elements,
        style={'width': '100%', 'height': '600px', 'background': '#f8f9fa'},
        stylesheet=[
            # 基础节点样式（所有节点继承）
            {'selector': 'node',
             'style': {
                 'content': 'data(label)',
                 'text-wrap': 'wrap',
                 'width': 50,  # 统一基础尺寸
                 'height': 50,
                 'text-valign': 'center',
                 'padding': '5px',
                 'font-size': '50px'
             }},

            # 特定节点定制样式
            {'selector': 'node[group = "O"]',  # 单比特算符节点
             'style': {
                 'border-width': 1,  # 加粗矩形边框
                 'border-color': '#000000',  # 强制黑色边框
                 'background-color': '#FFFFFF',  # 保持原有白色填充
                 'shape': 'rectangle' , # 确保形状正确
                 'width': 50,  # 调整宽度以区分形状
                 'height': 50
             }},
            {'selector': 'node[group = "MO"]',  # 多比特算符节点
             'style': {
                 'border-width': 1,  # 加粗矩形边框
                 'border-color': '#000000',  # 强制黑色边框
                 'background-color': '#FFFFFF',  # 保持原有白色填充
                 'shape': 'rectangle',  # 确保形状正确
                 'width': 50,  # 调整宽度以区分形状
                 'height': 1500
             }},
            {'selector': 'node[group = "p"]',  # 折线节点
             'style': {
                 'border-width': 1,  # 加粗矩形边框
                 'border-color': '#000000',  # 强制黑色边框
                 'background-color': '#000000',  # 保持原有白色填充
                 'shape': 'rectangle',  # 确保形状正确
                 'width': 1,  # 调整宽度以区分形状
                 'height': 1
             }},
            {'selector': 'node[group = "CO"]',  # 修正算符节点
             'style': {
                 'border-width': 1,  # 加粗矩形边框
                 'border-color': '#000000',  # 强制黑色边框
                 'background-color': '#FFFFFF',  # 保持原有白色填充
                 'shape': 'rectangle',  # 确保形状正确
                 'width': 50,  # 调整宽度以区分形状
                 'height': 400
             }},
            {'selector': 'node[group = "c"]',  # 控制节点
             'style': {
                 'border-width': 1,  # 加粗矩形边框
                 'border-color': '#000000',  # 强制黑色边框
                 'background-color': '#000000',  # 保持原有白色填充
                 'shape': 'ellipse' , # 确保形状正确
                 'width': 5,  # 调整宽度以区分形状
                 'height': 5
             }},
            # 特定节点定制样式
            {'selector': 'node[group = "XE"]',  # X错误节点
             'style': {
                 'border-width': 1,  # 加粗矩形边框
                 'border-color': '#000000',  # 强制黑色边框
                 'background-color': '#FF0000',  # 保持原有白色填充
                 'shape': 'rectangle',  # 确保形状正确
                 'width': 15,  # 调整宽度以区分形状
                 'height': 15
             }},
            {'selector': 'node[group = "ZE"]',  # Z错误节点
             'style': {
                 'border-width': 1,  # 加粗矩形边框
                 'border-color': '#000000',  # 强制黑色边框
                 'background-color': '#0000FF',  # 保持原有白色填充
                 'shape': 'rectangle',  # 确保形状正确
                 'width': 15,  # 调整宽度以区分形状
                 'height': 15
             }},
            {'selector': 'node[group = "E"]',  # XZ错误节点
             'style': {
                 'border-width': 1,  # 加粗矩形边框
                 'border-color': '#000000',  # 强制黑色边框
                 'background-color': '#000000',  # 保持原有白色填充
                 'shape': 'rectangle',  # 确保形状正确
                 'width': 15,  # 调整宽度以区分形状
                 'height': 15
             }},
            {'selector': 'node[group = "nE"]',  # 无错误节点
             'style': {
                 'border-width': 1,  # 加粗矩形边框
                 'border-color': '#000000',  # 强制黑色边框
                 'background-color': '#FFFFFF',  # 保持原有白色填充
                 'shape': 'rectangle',  # 确保形状正确
                 'width': 15,  # 调整宽度以区分形状
                 'height': 15
             }},
        ]
    )
])
if __name__ == '__main__':
    TGpri.run(host='0.0.0.0', port=8051, debug=True)  # 必须设置host参数
