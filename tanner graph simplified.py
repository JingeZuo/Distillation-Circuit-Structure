import dash
import dash_cytoscape as cyto
from dash import html
#%%
TGDeiso = dash.Dash(__name__)

elements = [
    #第一行X

    {'data': {'id': 'X16', 'label': 'X16', 'group': 'X'}, 'position': {'x': 1000, 'y': 0}},


    #第二行X

    {'data': {'id': 'X25', 'label': 'X25', 'group': 'X'}, 'position': {'x': 800, 'y':100}},


    # 第三行X

    {'data': {'id': 'CX378', 'label': 'CX378', 'group': 'C'}, 'position': {'x': 1300, 'y': 200}},
    {'data': {'id': 'X38', 'label': 'X38', 'group': 'X'}, 'position': {'x': 1400, 'y': 200}},
    {'data': {'source': 'X38', 'target': 'CX378'}},

    # 第四行X

    {'data': {'id': 'X44', 'label': 'X44', 'group': 'X'}, 'position': {'x': 600, 'y': 300}},


    # 第五行X

    {'data': {'id': 'CX567', 'label': 'CX567', 'group': 'C'}, 'position': {'x': 1100, 'y': 400}},
    {'data': {'id': 'X58', 'label': 'X58', 'group': 'X'}, 'position': {'x': 1400, 'y': 400}},
    {'data': {'source': 'X58', 'target': 'CX567'}},

    # 第六行X
    {'data': {'id': 'CX656', 'label': 'CX656', 'group': 'C'}, 'position': {'x': 900, 'y': 500}},
    {'data': {'id': 'X68', 'label': 'X68', 'group': 'X'}, 'position': {'x': 1400, 'y': 500}},
    {'data': {'source': 'X68', 'target': 'CX656'}},

    # 第七行X
    {'data': {'id': 'CX767', 'label': 'CX767', 'group': 'C'}, 'position': {'x': 1100, 'y': 600}},
    {'data': {'id': 'X78', 'label': 'X78', 'group': 'X'}, 'position': {'x': 1400, 'y': 600}},
    {'data': {'source': 'X78', 'target': 'CX767'}},

    # 第八行X
    {'data': {'id': 'X83', 'label': 'X83', 'group': 'X'}, 'position': {'x': 400, 'y':700}},

    # 第九行X
    {'data': {'id': 'CX978', 'label': 'CX978', 'group': 'C'}, 'position': {'x': 1300, 'y':800}},
    {'data': {'id': 'X98', 'label': 'X98', 'group': 'X'}, 'position': {'x': 1400, 'y':800}},
    {'data': {'source': 'X98', 'target': 'CX978'}},

    # 第10行X
    {'data': {'id': 'CX1078', 'label': 'CX1078', 'group': 'C'}, 'position': {'x': 1300, 'y':900}},
    {'data': {'id': 'X108', 'label': 'X108', 'group': 'X'}, 'position': {'x': 1400, 'y':900}},
    {'data': {'source': 'X108', 'target': 'CX1078'}},

    # 第11行X
    {'data': {'id': 'CX1167', 'label': 'CX1167', 'group': 'C'}, 'position': {'x': 1100, 'y':1000}},
    {'data': {'id': 'X118', 'label': 'X118', 'group': 'X'}, 'position': {'x': 1400, 'y':1000}},
    {'data': {'source': 'X118', 'target': 'CX1167'}},

    # 第12行X
    {'data': {'id': 'CX1278', 'label': 'CX1278', 'group': 'C'}, 'position': {'x': 1300, 'y':1100}},
    {'data': {'id': 'X128', 'label': 'X128', 'group': 'X'}, 'position': {'x': 1400, 'y':1100}},
    {'data': {'source': 'X128', 'target': 'CX1278'}},

    # 第13行X
    {'data': {'id': 'CX1367', 'label': 'CX1367', 'group': 'C'}, 'position': {'x': 1100, 'y': 1200}},
    {'data': {'id': 'X138', 'label': 'X138', 'group': 'X'}, 'position': {'x': 1400, 'y': 1200}},
    {'data': {'source': 'X138', 'target': 'CX1367'}},

    # 第14行X
    {'data': {'id': 'CX1456', 'label': 'CX1456', 'group': 'C'}, 'position': {'x': 900, 'y': 1300}},
    {'data': {'id': 'X148', 'label': 'X148', 'group': 'X'}, 'position': {'x': 1400, 'y': 1300}},
    {'data': {'source': 'X148', 'target': 'CX1456'}},

    # 第15行X
    {'data': {'id': 'CX1523', 'label': 'CX1523', 'group': 'C'}, 'position': {'x': 300, 'y': 1400}},
    {'data': {'id': 'X157', 'label': 'X157', 'group': 'X'}, 'position': {'x': 1200, 'y': 1400}},
    {'data': {'source': 'X157', 'target': 'CX1523'}},

    # 第16行X
    {'data': {'id': 'X162', 'label': 'X162', 'group': 'X'}, 'position': {'x': 200, 'y': 1500}},

    # 第1行Z
    {'data': {'id': 'CZ167', 'label': 'CZ167', 'group': 'C'}, 'position': {'x': 2900, 'y': 0}},
    {'data': {'id': 'Z18', 'label': 'Z18', 'group': 'Z'}, 'position': {'x': 3200, 'y': 0}},
    {'data': {'source': 'Z18', 'target': 'CZ167'}},

    #第2行Z
    {'data': {'id': 'CZ256', 'label': 'CZ256', 'group': 'C'}, 'position': {'x': 2700, 'y': 100}},
    {'data': {'id': 'Z28', 'label': 'Z28', 'group': 'Z'}, 'position': {'x': 3200, 'y': 100}},
    {'data': {'source': 'Z28', 'target': 'CZ256'}},

    # 第3行Z
    {'data': {'id': 'Z35', 'label': 'Z35', 'group': 'Z'}, 'position': {'x': 2600, 'y': 200}},

    # 第4行Z
    {'data': {'id': 'CZ445', 'label': 'CZ445', 'group': 'C'}, 'position': {'x': 2500, 'y': 300}},
    {'data': {'id': 'Z48', 'label': 'Z48', 'group': 'Z'}, 'position': {'x': 3200, 'y': 300}},
    {'data': {'source': 'Z48', 'target': 'CZ445'}},

    # 第5行Z
    {'data': {'id': 'Z54', 'label': 'Z54', 'group': 'Z'}, 'position': {'x': 2400, 'y': 400}},

    # 第6行Z
    {'data': {'id': 'Z64', 'label': 'Z64', 'group': 'Z'}, 'position': {'x': 2400, 'y': 500}},

    # 第7行Z
    {'data': {'id': 'Z74', 'label': 'Z74', 'group': 'Z'}, 'position': {'x': 2400, 'y': 600}},

    # 第8行Z
    {'data': {'id': 'CZ834', 'label': 'CZ834', 'group': 'C'}, 'position': {'x': 2300, 'y': 700}},
    {'data': {'id': 'Z88', 'label': 'Z88', 'group': 'Z'}, 'position': {'x': 3200, 'y': 700}},
    {'data': {'source': 'Z88', 'target': 'CZ834'}},

    # 第9行Z
    {'data': {'id': 'Z93', 'label': 'Z93', 'group': 'Z'}, 'position': {'x': 2200, 'y': 800}},

    # 第10行Z
    {'data': {'id': 'Z103', 'label': 'Z103', 'group': 'Z'}, 'position': {'x': 2200, 'y': 900}},

    # 第11行Z
    {'data': {'id': 'Z113', 'label': 'Z113', 'group': 'Z'}, 'position': {'x': 2200, 'y': 1000}},

    # 第12行Z
    {'data': {'id': 'Z123', 'label': 'Z123', 'group': 'Z'}, 'position': {'x': 2200, 'y': 1100}},

    # 第13行Z
    {'data': {'id': 'Z133', 'label': 'Z133', 'group': 'Z'}, 'position': {'x': 2200, 'y': 1200}},

    # 第14行Z
    {'data': {'id': 'Z143', 'label': 'Z143', 'group': 'Z'}, 'position': {'x': 2200, 'y': 1300}},

    # 第15行Z
    {'data': {'id': 'Z152', 'label': 'Z152', 'group': 'Z'}, 'position': {'x': 2000, 'y': 1400}},
    {'data': {'id': 'CZ1578', 'label': 'CZ1578', 'group': 'C'}, 'position': {'x': 3100, 'y': 1400}},
    {'data': {'id': 'Z158', 'label': 'Z158', 'group': 'Z'}, 'position': {'x': 3200, 'y': 1400}},
    {'data': {'source': 'Z152', 'target': 'CZ1578'}},
    {'data': {'source': 'Z158', 'target': 'CZ1578'}},

    # 第16行Z
    {'data': {'id': 'CZ1623', 'label': 'CZ1623', 'group': 'C'}, 'position': {'x': 2100, 'y': 1500}},
    {'data': {'id': 'Z168', 'label': 'Z168', 'group': 'Z'}, 'position': {'x': 3200, 'y': 1500}},
    {'data': {'source': 'Z168', 'target': 'CZ1623'}},
]
CNOT1_edges =[{'data': {'source': 'X162', 'target': 'CX1523'}},
              {'data': {'source': 'Z152', 'target': 'CZ1623'}},]

CNOT2X = ['CX978', 'CX1078', 'CX1167', 'CX1278', 'CX1367', 'CX1456', 'CX1523']  # 按需扩展
CNOT2X_edges = [{'data': {'source': 'X83','target': target,}} for target in CNOT2X]
CNOT2Z = ['Z93', 'Z103', 'Z113', 'Z123', 'Z133', 'Z143', 'Z152']
CNOT2Z_edges = [{'data': {'source': 'CZ834','target': target,}} for target in CNOT2Z]

CNOT3X = ['CX567', 'CX656', 'CX767', 'CX1278', 'CX1367', 'CX1456', 'CX1523']  # 按需扩展
CNOT3X_edges = [{'data': {'source': 'X44','target': target,}} for target in CNOT3X]
CNOT3Z = ['Z54', 'Z64', 'Z74', 'Z123', 'Z133', 'Z143', 'Z152']
CNOT3Z_edges = [{'data': {'source': 'CZ445','target': target,}} for target in CNOT3Z]

CNOT4X = ['CX378', 'CX656', 'CX767', 'CX1078', 'CX1167', 'CX1456', 'CX1523']  # 按需扩展
CNOT4X_edges = [{'data': {'source': 'X25','target': target,}} for target in CNOT4X]
CNOT4Z = ['Z35', 'Z64', 'Z74', 'Z103', 'Z113', 'Z143', 'Z152']
CNOT4Z_edges = [{'data': {'source': 'CZ256','target': target,}} for target in CNOT4Z]

CNOT5X = ['CX378', 'CX567', 'CX767', 'CX978', 'CX1167', 'CX1367', 'CX1523']  # 按需扩展
CNOT5X_edges = [{'data': {'source': 'X16','target': target,}} for target in CNOT5X]
CNOT5Z = ['Z35', 'Z54', 'Z74', 'Z93', 'Z113', 'Z133', 'Z152']
CNOT5Z_edges = [{'data': {'source': 'CZ167','target': target,}} for target in CNOT5Z]

CNOT6X = ['CX378', 'CX567', 'CX656', 'CX978', 'CX1078', 'CX1278']  # 按需扩展
CNOT6X_edges = [{'data': {'source': 'X157','target': target,}} for target in CNOT6X]
CNOT6Z = ['Z35', 'Z54', 'Z64', 'Z93', 'Z103', 'Z123']
CNOT6Z_edges = [{'data': {'source': 'CZ1578','target': target,}} for target in CNOT6Z]
elements.extend(CNOT1_edges+CNOT2X_edges+CNOT2Z_edges+CNOT3X_edges+CNOT3Z_edges+CNOT4X_edges+CNOT4Z_edges+
                CNOT5X_edges+CNOT5Z_edges+CNOT6X_edges+CNOT6Z_edges)
TGDeiso.layout = html.Div([
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
                 'width': 50,  # 统一基础尺寸
                 'height': 50,
                 'text-valign': 'center'
             }},

            # 特定节点定制样式
            {'selector': 'node[group = "C"]',  # 矩形节点
             'style': {
                 'border-width': 1,  # 加粗矩形边框
                 'border-color': '#000000',  # 强制黑色边框
                 'background-color': '#FFFFFF',  # 保持原有白色填充
                 'shape': 'rectangle' , # 确保形状正确
                 'width': 50,  # 调整宽度以区分形状
                 'height': 50
             }},
            {
                'selector': '[group = "X"]',
                'style': {'background-color': '#FF0000',
                          'shape': 'ellipse'}
            },
            {
                'selector': '[group = "Z"]',
                'style': {'background-color': '#0000FF',
                          'shape': 'ellipse'}
            },

            {'selector': 'edge',
             'style': {
                 'curve-style': 'bezier',
                 'line-color': '#9E9E9E'
             }}
        ]
    )
])


if __name__ == '__main__':
    TGDeiso.run(host='0.0.0.0', port=8051, debug=True)  # 必须设置host参数
