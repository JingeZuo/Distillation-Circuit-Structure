import dash
import dash_cytoscape as cyto
from dash import html
#%%
TGiso = dash.Dash(__name__)

elements = [
    #第一行X
    {'data': {'id': 'X16', 'label': 'X16', 'group': 'X'}, 'position': {'x': 1100, 'y': 0}},

    #第二行X
    {'data': {'id': 'X26', 'label': 'X26', 'group': 'X'}, 'position': {'x': 1100, 'y':100}},

    # 第三行X
    {'data': {'id': 'X36', 'label': 'X36', 'group': 'X'}, 'position': {'x': 1100, 'y': 200}},

    # 第四行X
    {'data': {'id': 'CX456', 'label': 'CX456', 'group': 'C'}, 'position': {'x': 1000, 'y': 300}},
    {'data': {'id': 'X46', 'label': 'X46', 'group': 'X'}, 'position': {'x': 1100, 'y': 300}},
    {'data': {'source': 'X46', 'target': 'CX456'}},

    # 第五行X
    {'data': {'id': 'CX545', 'label': 'CX545', 'group': 'C'}, 'position': {'x': 800, 'y': 400}},
    {'data': {'id': 'X56', 'label': 'X56', 'group': 'X'}, 'position': {'x': 1100, 'y': 400}},
    {'data': {'source': 'X56', 'target': 'CX545'}},

    # 第六行X
    {'data': {'id': 'CX656', 'label': 'CX656', 'group': 'C'}, 'position': {'x': 1000, 'y': 500}},
    {'data': {'id': 'X66', 'label': 'X66', 'group': 'X'}, 'position': {'x': 1100, 'y': 500}},
    {'data': {'source': 'X66', 'target': 'CX656'}},

    # 第七行X
    {'data': {'id': 'CX712', 'label': 'CX712', 'group': 'C'}, 'position': {'x': 200, 'y': 600}},
    {'data': {'id': 'X72', 'label': 'X72', 'group': 'X'}, 'position': {'x': 300, 'y': 600}},
    {'data': {'id': 'CX745', 'label': 'CX745', 'group': 'C'}, 'position': {'x': 800, 'y': 600}},
    {'data': {'id': 'X76', 'label': 'X76', 'group': 'X'}, 'position': {'x': 1100, 'y': 600}},
    {'data': {'source': 'X72', 'target': 'CX712'}},
    {'data': {'source': 'X72', 'target': 'CX745'}},
    {'data': {'source': 'X76', 'target': 'CX745'}},

    # 第八行X
    {'data': {'id': 'X81', 'label': 'X81', 'group': 'X'}, 'position': {'x': 100, 'y':700}},


    # 第1行Z
    {'data': {'id': 'CZ167', 'label': 'CZ167', 'group': 'C'}, 'position': {'x': 3100, 'y': 100}},

    #第2行Z
    {'data': {'id': 'CZ267', 'label': 'CZ267', 'group': 'C'}, 'position': {'x': 3100, 'y': 200}},

    # 第3行Z
    {'data': {'id': 'CZ367', 'label': 'CZ367', 'group': 'C'}, 'position': {'x': 3100, 'y': 300}},

    # 第4行Z
    {'data': {'id': 'Z42', 'label': 'Z42', 'group': 'Z'}, 'position': {'x': 2200, 'y': 400}},
    {'data': {'id': 'CZ467', 'label': 'CZ467', 'group': 'C'}, 'position': {'x': 3100, 'y': 400}},
    {'data': {'source': 'Z42', 'target': 'CZ467'}},

    # 第5行Z
    {'data': {'id': 'Z52', 'label': 'Z52', 'group': 'Z'}, 'position': {'x': 2200, 'y': 500}},
    {'data': {'id': 'CZ567', 'label': 'CZ567', 'group': 'C'}, 'position': {'x': 3100, 'y': 500}},
    {'data': {'source': 'Z52', 'target': 'CZ567'}},

    # 第6行Z
    {'data': {'id': 'Z63', 'label': 'Z63', 'group': 'Z'}, 'position': {'x': 2400, 'y': 600}},
    {'data': {'id': 'CZ667', 'label': 'CZ667', 'group': 'C'}, 'position': {'x': 3100, 'y': 600}},
    {'data': {'source': 'Z63', 'target': 'CZ667'}},

    # 第7行Z
    {'data': {'id': 'Z71', 'label': 'Z71', 'group': 'Z'}, 'position': {'x': 2000, 'y': 700}},
    {'data': {'id': 'CZ723', 'label': 'CZ723', 'group': 'C'}, 'position': {'x': 2300, 'y': 700}},
    {'data': {'id': 'Z74', 'label': 'Z74', 'group': 'Z'}, 'position': {'x': 2600, 'y': 700}},
    {'data': {'id': 'CZ767', 'label': 'CZ767', 'group': 'C'}, 'position': {'x': 3100, 'y': 700}},
    {'data': {'source': 'Z71', 'target': 'CZ723'}},
    {'data': {'source': 'Z74', 'target': 'CZ723'}},
    {'data': {'source': 'Z74', 'target': 'CZ767'}},


    # 第8行Z
    {'data': {'id': 'CZ812', 'label': 'CZ812', 'group': 'C'}, 'position': {'x': 2100, 'y': 800}},

]

CNOT1_edges =[{'data': {'source': 'X81', 'target': 'CX712'}},
              {'data': {'source': 'Z71', 'target': 'CZ812'}},]

CNOT2X = ['CX456', 'CX545']  # 按需扩展
CNOT2X_edges = [{'data': {'source': 'X72','target': target,}} for target in CNOT2X]
CNOT2Z = ['Z42', 'Z52']
CNOT2Z_edges = [{'data': {'source': 'CZ723','target': target,}} for target in CNOT2Z]

CNOT3X = ['CX456', 'CX545', 'CX656']  # 按需扩展
CNOT3X_edges = [{'data': {'source': 'X36','target': target,}} for target in CNOT3X]
CNOT3Z = ['Z42', 'Z52', 'Z63']
CNOT3Z_edges = [{'data': {'source': 'CZ367','target': target,}} for target in CNOT3Z]

CNOT4X = ['CX545', 'CX656', 'CX745']  # 按需扩展
CNOT4X_edges = [{'data': {'source': 'X26','target': target,}} for target in CNOT4X]
CNOT4Z = ['Z52', 'Z63', 'Z74']
CNOT4Z_edges = [{'data': {'source': 'CZ267','target': target,}} for target in CNOT4Z]

CNOT5X = ['CX456', 'CX656', 'CX745']  # 按需扩展
CNOT5X_edges = [{'data': {'source': 'X16','target': target,}} for target in CNOT5X]
CNOT5Z = ['Z42', 'Z63', 'Z74']
CNOT5Z_edges = [{'data': {'source': 'CZ167','target': target,}} for target in CNOT5Z]

S = [{'data': {'source': 'X16', 'target': 'CZ167'}},
     {'data': {'source': 'X26', 'target': 'CZ267'}},
     {'data': {'source': 'X36', 'target': 'CZ367'}},
     {'data': {'source': 'X46', 'target': 'CZ467'}},
     {'data': {'source': 'X56', 'target': 'CZ567'}},
     {'data': {'source': 'X66', 'target': 'CZ667'}},
     {'data': {'source': 'X76', 'target': 'CZ767'}},]

elements.extend(CNOT1_edges+CNOT2X_edges+CNOT2Z_edges+CNOT3X_edges+CNOT3Z_edges+CNOT4X_edges+CNOT4Z_edges+
                CNOT5X_edges+CNOT5Z_edges+S)
TGiso.layout = html.Div([
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
    TGiso.run(host='0.0.0.0', port=8052, debug=True)  # 必须设置host参数
