import dash
import dash_cytoscape as cyto
from dash import html
#%%
#15to1原始tanner graph
TGpri = dash.Dash(__name__)

elements = [
    #第一行X
    {'data': {'id': 'X16', 'label': 'X16', 'group': 'X'}, 'position': {'x': 0, 'y': 0}},

    #第二行X

    {'data': {'id': 'X25', 'label': 'X25', 'group': 'X'}, 'position': {'x': 0, 'y':100}},

    # 第三行X

    {'data': {'id': 'X34', 'label': 'X34', 'group': 'X'}, 'position': {'x': 0, 'y': 200}},

    # 第四行X
    {'data': {'id': 'CX467', 'label': 'CX467', 'group': 'C'}, 'position': {'x': 1200, 'y': 300}},
    {'data': {'id': 'X47', 'label': 'X47', 'group': 'X'}, 'position': {'x': 0, 'y': 300}},
    {'data': {'source': 'X47', 'target': 'CX467'}},

    # 第五行X
    {'data': {'id': 'CX556', 'label': 'CX556', 'group': 'C'}, 'position': {'x': 1200, 'y': 400}},
    {'data': {'id': 'X57', 'label': 'X57', 'group': 'X'}, 'position': {'x': 0, 'y': 400}},
    {'data': {'source': 'X57', 'target': 'CX556'}},

    # 第六行X
    {'data': {'id': 'CX667', 'label': 'CX667', 'group': 'C'}, 'position': {'x': 1200, 'y': 500}},
    {'data': {'id': 'X67', 'label': 'X67', 'group': 'X'}, 'position': {'x': 0, 'y': 500}},
    {'data': {'source': 'X67', 'target': 'CX667'}},

    # 第七行X
    {'data': {'id': 'CX723', 'label': 'CX723', 'group': 'C'}, 'position': {'x': 1200, 'y': 600}},
    {'data': {'id': 'X73', 'label': 'X73', 'group': 'X'}, 'position': {'x': 0, 'y': 600}},
    {'data': {'id': 'CX767', 'label': 'CX767', 'group': 'C'}, 'position': {'x': 1100, 'y': 600}},
    {'data': {'id': 'X77', 'label': 'X77', 'group': 'X'}, 'position': {'x': 100, 'y': 600}},
    {'data': {'source': 'X73', 'target': 'CX723'}},
    {'data': {'source': 'X73', 'target': 'CX767'}},
    {'data': {'source': 'X77', 'target': 'CX767'}},

    # 第八行X
    {'data': {'id': 'X82', 'label': 'X82', 'group': 'X'}, 'position': {'x': 0, 'y':700}},

    # 第1行Z
    {'data': {'id': 'CZ167', 'label': 'CZ167', 'group': 'C'}, 'position': {'x': 3000, 'y': 0}},
    {'data': {'id': 'Z17', 'label': 'Z17', 'group': 'Z'}, 'position': {'x': 1900, 'y': 0}},
    {'data': {'source': 'Z17', 'target': 'CZ167'}},
    #第2行Z
    {'data': {'id': 'CZ256', 'label': 'CZ256', 'group': 'C'}, 'position': {'x': 3000, 'y': 100}},
    {'data': {'id': 'Z27', 'label': 'Z27', 'group': 'Z'}, 'position': {'x': 1900, 'y': 100}},
    {'data': {'source': 'Z27', 'target': 'CZ256'}},

    # 第3行Z
    {'data': {'id': 'CZ345', 'label': 'CZ345', 'group': 'C'}, 'position': {'x': 3000, 'y': 200}},
    {'data': {'id': 'Z37', 'label': 'Z37', 'group': 'Z'}, 'position': {'x': 1900, 'y': 200}},
    {'data': {'source': 'Z37', 'target': 'CZ345'}},

    # 第4行Z
    {'data': {'id': 'Z43', 'label': 'Z43', 'group': 'Z'}, 'position': {'x': 1900, 'y': 300}},

    # 第5行Z
    {'data': {'id': 'Z53', 'label': 'Z53', 'group': 'Z'}, 'position': {'x': 1900, 'y': 400}},

    # 第6行Z
    {'data': {'id': 'Z64', 'label': 'Z64', 'group': 'Z'}, 'position': {'x': 1900, 'y': 500}},

    # 第7行Z
    {'data': {'id': 'Z72', 'label': 'Z72', 'group': 'Z'}, 'position': {'x': 1900, 'y': 600}},
    {'data': {'id': 'CZ734', 'label': 'CZ734', 'group': 'C'}, 'position': {'x': 3000, 'y': 600}},
    {'data': {'id': 'Z76', 'label': 'Z76', 'group': 'Z'}, 'position': {'x': 2000, 'y': 600}},
    {'data': {'source': 'Z72', 'target': 'CZ734'}},
    {'data': {'source': 'Z76', 'target': 'CZ734'}},

    # 第8行Z
    {'data': {'id': 'CZ823', 'label': 'CZ823', 'group': 'C'}, 'position': {'x': 3000, 'y': 700}},

]

CNOT1_edges =[{'data': {'source': 'X82', 'target': 'CX723'}},
              {'data': {'source': 'Z72', 'target': 'CZ823'}},]

CNOT2X = ['CX467', 'CX556']  # 按需扩展
CNOT2X_edges = [{'data': {'source': 'X73','target': target,}} for target in CNOT2X]
CNOT2Z = ['Z43', 'Z53']
CNOT2Z_edges = [{'data': {'source': 'CZ734','target': target,}} for target in CNOT2Z]

CNOT3X = ['CX467', 'CX556', 'CX667']  # 按需扩展
CNOT3X_edges = [{'data': {'source': 'X34','target': target,}} for target in CNOT3X]
CNOT3Z = ['Z43', 'Z53', 'Z64']
CNOT3Z_edges = [{'data': {'source': 'CZ345','target': target,}} for target in CNOT3Z]

CNOT4X = ['CX556', 'CX667', 'CX767']  # 按需扩展
CNOT4X_edges = [{'data': {'source': 'X25','target': target,}} for target in CNOT4X]
CNOT4Z = ['Z53', 'Z64', 'Z76']
CNOT4Z_edges = [{'data': {'source': 'CZ256','target': target,}} for target in CNOT4Z]

CNOT5X = ['CX467', 'CX667', 'CX767']  # 按需扩展
CNOT5X_edges = [{'data': {'source': 'X16','target': target,}} for target in CNOT5X]
CNOT5Z = ['Z43', 'Z64', 'Z76']
CNOT5Z_edges = [{'data': {'source': 'CZ167','target': target,}} for target in CNOT5Z]
elements.extend(CNOT1_edges+CNOT2X_edges+CNOT2Z_edges+CNOT3X_edges+CNOT3Z_edges+CNOT4X_edges+CNOT4Z_edges+
                CNOT5X_edges+CNOT5Z_edges)
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
    TGpri.run(host='0.0.0.0', port=8052, debug=True)  # 必须设置host参数
