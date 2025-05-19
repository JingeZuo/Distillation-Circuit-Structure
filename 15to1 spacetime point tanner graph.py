import dash
import dash_cytoscape as cyto
from dash import html
#%%
TGpri = dash.Dash(__name__)
elements = [
    #第一行
{'data': {'id': 'q1', 'label': '+','group': 'q'}, 'position': {'x': 0, 'y': 0}},
{'data': {'id': 'E11','group': 'nE'}, 'position': {'x': 450, 'y': 0}},
{'data': {'id': 'c1','group': 'c'}, 'position': {'x': 500, 'y': 0}},
{'data': {'id': 'E12','group': 'nE'}, 'position': {'x': 550, 'y': 0}},
{'data': {'id': 'T1','label': 'T','group': 'T'}, 'position': {'x': 700, 'y': 0}},
{'data': {'source': 'q1', 'target': 'c1'}},
{'data': {'source': 'c1', 'target': 'T1'}},
    #第二行
{'data': {'id': 'q2', 'label': '+','group': 'q'}, 'position': {'x': 0, 'y': 100}},
{'data': {'id': 'E21','group': 'nE'}, 'position': {'x':350, 'y': 100}},
{'data': {'id': 'c2','group': 'c'}, 'position': {'x': 400, 'y': 100}},
{'data': {'id': 'E22','group': 'nE'}, 'position': {'x':450, 'y': 100}},
{'data': {'id': 'T2','label': 'T','group': 'T'}, 'position': {'x': 700, 'y': 100}},
{'data': {'source': 'q2', 'target': 'c2'}},
{'data': {'source': 'c2', 'target': 'T2'}},
    #第三行
{'data': {'id': 'q3', 'label': '0','group': 'q'}, 'position': {'x': 0, 'y': 200}},
{'data': {'id': 'E31','group': 'nE'}, 'position': {'x': 350, 'y': 200}},
{'data': {'id': 't34','group': 't'}, 'position': {'x': 400, 'y': 200}},
{'data': {'id': 'E32','group': 'nE'}, 'position': {'x': 450, 'y': 200}},
{'data': {'id': 't35','group': 't'}, 'position': {'x': 500, 'y': 200}},
{'data': {'id': 'E33','group': 'nE'}, 'position': {'x': 550, 'y': 200}},
{'data': {'id': 't36','group': 't'}, 'position': {'x': 600, 'y': 200}},
{'data': {'id': 'E34','group': 'nE'}, 'position': {'x': 650, 'y': 200}},
{'data': {'id': 'T3','label': 'T','group': 'T'}, 'position': {'x': 700, 'y': 200}},
{'data': {'source': 'q3', 'target': 't34'}},
{'data': {'source': 't34', 'target': 't35'}},
{'data': {'source': 't35', 'target': 't36'}},
{'data': {'source': 't36', 'target': 'T3'}},
    #第四行
{'data': {'id': 'q4', 'label': '+','group': 'q'}, 'position': {'x': 0, 'y': 300}},
{'data': {'id': 'E41','group': 'nE'}, 'position': {'x': 250, 'y': 300}},
{'data': {'id': 'c4','group': 'c'}, 'position': {'x': 300, 'y': 300}},
{'data': {'id': 'E42','group': 'nE'}, 'position': {'x': 350, 'y': 300}},
{'data': {'id': 'T4','label': 'T','group': 'T'}, 'position': {'x': 700, 'y': 300}},
{'data': {'source': 'q4', 'target': 'c4'}},
{'data': {'source': 'c4', 'target': 'T4'}},
    #第五行
{'data': {'id': 'q5', 'label': '0','group': 'q'}, 'position': {'x': 0, 'y': 400}},
{'data': {'id': 'E51','group': 'nE'}, 'position': {'x': 250, 'y': 400}},
{'data': {'id': 't53','group': 't'}, 'position': {'x': 300, 'y': 400}},
{'data': {'id': 'E52','group': 'nE'}, 'position': {'x': 400, 'y': 400}},
{'data': {'id': 't55','group': 't'}, 'position': {'x': 500, 'y': 400}},
{'data': {'id': 'E53','group': 'nE'}, 'position': {'x': 550, 'y': 400}},
{'data': {'id': 't56','group': 't'}, 'position': {'x': 600, 'y': 400}},
{'data': {'id': 'E54','group': 'nE'}, 'position': {'x': 650, 'y': 400}},
{'data': {'id': 'T5','label': 'T','group': 'T'}, 'position': {'x': 700, 'y': 400}},
{'data': {'source': 'q5', 'target': 't53'}},
{'data': {'source': 't53', 'target': 't55'}},
{'data': {'source': 't55', 'target': 't56'}},
{'data': {'source': 't56', 'target': 'T5'}},
    #第六行
{'data': {'id': 'q6', 'label': '0','group': 'q'}, 'position': {'x': 0, 'y': 500}},
{'data': {'id': 'E61','group': 'nE'}, 'position': {'x': 250, 'y': 500}},
{'data': {'id': 't63','group': 't'}, 'position': {'x': 300, 'y': 500}},
{'data': {'id': 'E62','group': 'nE'}, 'position': {'x': 350, 'y': 500}},
{'data': {'id': 't64','group': 't'}, 'position': {'x': 400, 'y': 500}},
{'data': {'id': 'E63','group': 'nE'}, 'position': {'x': 500, 'y': 500}},
{'data': {'id': 't66','group': 't'}, 'position': {'x': 600, 'y': 500}},
{'data': {'id': 'E64','group': 'nE'}, 'position': {'x': 650, 'y': 500}},
{'data': {'id': 'T6','label': 'T','group': 'T'}, 'position': {'x': 700, 'y': 500}},
{'data': {'source': 'q6', 'target': 't63'}},
{'data': {'source': 't63', 'target': 't64'}},
{'data': {'source': 't64', 'target': 't66'}},
{'data': {'source': 't66', 'target': 'T6'}},
    #第七行
{'data': {'id': 'q7', 'label': '0','group': 'q'}, 'position': {'x': 0, 'y': 600}},
{'data': {'id': 'E71','group': 'nE'}, 'position': {'x': 250, 'y': 600}},
{'data': {'id': 't73','group': 't'}, 'position': {'x': 300, 'y': 600}},
{'data': {'id': 'E72','group': 'nE'}, 'position': {'x': 350, 'y': 600}},
{'data': {'id': 't74','group': 't'}, 'position': {'x': 400, 'y': 600}},
{'data': {'id': 'E73','group': 'nE'}, 'position': {'x': 450, 'y': 600}},
{'data': {'id': 't75','group': 't'}, 'position': {'x': 500, 'y': 600}},
{'data': {'id': 'E74','group': 'nE'}, 'position': {'x': 550, 'y': 600}},
{'data': {'id': 'T7','label': 'T','group': 'T'}, 'position': {'x': 700, 'y': 600}},
{'data': {'source': 'q7', 'target': 't73'}},
{'data': {'source': 't73', 'target': 't74'}},
{'data': {'source': 't74', 'target': 't75'}},
{'data': {'source': 't75', 'target': 'T7'}},
    #第八行
{'data': {'id': 'q8', 'label': '+','group': 'q'}, 'position': {'x': 0, 'y': 700}},
{'data': {'id': 'E81','group': 'nE'}, 'position': {'x': 150, 'y': 700}},
{'data': {'id': 'c8','group': 'c'}, 'position': {'x': 200, 'y': 700}},
{'data': {'id': 'E82','group': 'nE'}, 'position': {'x': 250, 'y': 700}},
{'data': {'id': 'T8','label': 'T','group': 'T'}, 'position': {'x': 700, 'y': 700}},
{'data': {'source': 'q8', 'target': 'c8'}},
{'data': {'source': 'c8', 'target': 'T8'}},
    #第九行
{'data': {'id': 'q9', 'label': '0','group': 'q'}, 'position': {'x': 0, 'y': 800}},
{'data': {'id': 'E91','group': 'nE'}, 'position': {'x': 150, 'y': 800}},
{'data': {'id': 't92','group': 't'}, 'position': {'x': 200, 'y': 800}},
{'data': {'id': 'E92','group': 'nE'}, 'position': {'x': 350, 'y': 800}},
{'data': {'id': 't95','group': 't'}, 'position': {'x': 500, 'y': 800}},
{'data': {'id': 'E93','group': 'nE'}, 'position': {'x': 550, 'y': 800}},
{'data': {'id': 't96','group': 't'}, 'position': {'x': 600, 'y': 800}},
{'data': {'id': 'E94','group': 'nE'}, 'position': {'x': 650, 'y': 800}},
{'data': {'id': 'T9','label': 'T','group': 'T'}, 'position': {'x': 700, 'y': 800}},
{'data': {'source': 'q9', 'target': 't95'}},
{'data': {'source': 't92', 'target': 't95'}},
{'data': {'source': 't95', 'target': 't96'}},
{'data': {'source': 't96', 'target': 'T9'}},
    #第十行
{'data': {'id': 'q10', 'label': '0','group': 'q'}, 'position': {'x': 0, 'y': 900}},
{'data': {'id': 'E101','group': 'nE'}, 'position': {'x': 150, 'y': 900}},
{'data': {'id': 't102','group': 't'}, 'position': {'x': 200, 'y': 900}},
{'data': {'id': 'E102','group': 'nE'}, 'position': {'x': 300, 'y': 900}},
{'data': {'id': 't104','group': 't'}, 'position': {'x': 400, 'y': 900}},
{'data': {'id': 'E103','group': 'nE'}, 'position': {'x': 500, 'y': 900}},
{'data': {'id': 't106','group': 't'}, 'position': {'x': 600, 'y': 900}},
{'data': {'id': 'E104','group': 'nE'}, 'position': {'x': 650, 'y': 900}},
{'data': {'id': 'T10','label': 'T','group': 'T'}, 'position': {'x': 700, 'y': 900}},
{'data': {'source': 'q10', 'target': 't102'}},
{'data': {'source': 't102', 'target': 't104'}},
{'data': {'source': 't104', 'target': 't106'}},
{'data': {'source': 't106', 'target': 'T10'}},
    #第11行
{'data': {'id': 'q11', 'label': '0','group': 'q'}, 'position': {'x': 0, 'y': 1000}},
{'data': {'id': 'E111','group': 'nE'}, 'position': {'x': 150, 'y': 1000}},
{'data': {'id': 't112','group': 't'}, 'position': {'x': 200, 'y': 1000}},
{'data': {'id': 'E112','group': 'nE'}, 'position': {'x': 300, 'y': 1000}},
{'data': {'id': 't114','group': 't'}, 'position': {'x': 400, 'y': 1000}},
{'data': {'id': 'E113','group': 'nE'}, 'position': {'x': 450, 'y': 1000}},
{'data': {'id': 't115','group': 't'}, 'position': {'x': 500, 'y': 1000}},
{'data': {'id': 'E114','group': 'nE'}, 'position': {'x': 550, 'y': 1000}},
{'data': {'id': 'T11','label': 'T','group': 'T'}, 'position': {'x': 700, 'y': 1000}},
{'data': {'source': 'q11', 'target': 't112'}},
{'data': {'source': 't112', 'target': 't114'}},
{'data': {'source': 't114', 'target': 't115'}},
{'data': {'source': 't115', 'target': 'T11'}},
    #第12行
{'data': {'id': 'q12', 'label': '0','group': 'q'}, 'position': {'x': 0, 'y': 1100}},
{'data': {'id': 'E121','group': 'nE'}, 'position': {'x': 150, 'y': 1100}},
{'data': {'id': 't122','group': 't'}, 'position': {'x': 200, 'y': 1100}},
{'data': {'id': 'E122','group': 'nE'}, 'position': {'x': 250, 'y': 1100}},
{'data': {'id': 't123','group': 't'}, 'position': {'x': 300, 'y': 1100}},
{'data': {'id': 'E123','group': 'nE'}, 'position': {'x': 450, 'y': 1100}},
{'data': {'id': 't126','group': 't'}, 'position': {'x': 600, 'y': 1100}},
{'data': {'id': 'E124','group': 'nE'}, 'position': {'x': 650, 'y': 1100}},
{'data': {'id': 'T12','label': 'T','group': 'T'}, 'position': {'x': 700, 'y': 1100}},
{'data': {'source': 'q12', 'target': 't122'}},
{'data': {'source': 't122', 'target': 't123'}},
{'data': {'source': 't123', 'target': 't126'}},
{'data': {'source': 't126', 'target': 'T12'}},
    #第13行
{'data': {'id': 'q13', 'label': '0','group': 'q'}, 'position': {'x': 0, 'y': 1200}},
{'data': {'id': 'E131','group': 'nE'}, 'position': {'x': 150, 'y': 1200}},
{'data': {'id': 't132','group': 't'}, 'position': {'x': 200, 'y': 1200}},
{'data': {'id': 'E132','group': 'nE'}, 'position': {'x': 250, 'y': 1200}},
{'data': {'id': 't133','group': 't'}, 'position': {'x': 300, 'y': 1200}},
{'data': {'id': 'E133','group': 'nE'}, 'position': {'x': 400, 'y': 1200}},
{'data': {'id': 't135','group': 't'}, 'position': {'x': 500, 'y': 1200}},
{'data': {'id': 'E134','group': 'nE'}, 'position': {'x': 550, 'y': 1200}},
{'data': {'id': 'T13','label': 'T','group': 'T'}, 'position': {'x': 700, 'y': 1200}},
{'data': {'source': 'q13', 'target': 't132'}},
{'data': {'source': 't132', 'target': 't133'}},
{'data': {'source': 't133', 'target': 't135'}},
{'data': {'source': 't135', 'target': 'T13'}},
    #第14行
{'data': {'id': 'q14', 'label': '0','group': 'q'}, 'position': {'x': 0, 'y': 1300}},
{'data': {'id': 'E141','group': 'nE'}, 'position': {'x': 150, 'y': 1300}},
{'data': {'id': 't142','group': 't'}, 'position': {'x': 200, 'y': 1300}},
{'data': {'id': 'E142','group': 'nE'}, 'position': {'x': 250, 'y': 1300}},
{'data': {'id': 't143','group': 't'}, 'position': {'x': 300, 'y': 1300}},
{'data': {'id': 'E143','group': 'nE'}, 'position': {'x': 350, 'y': 1300}},
{'data': {'id': 't144','group': 't'}, 'position': {'x': 400, 'y': 1300}},
{'data': {'id': 'E144','group': 'nE'}, 'position': {'x': 450, 'y': 1300}},
{'data': {'id': 'T14','label': 'T','group': 'T'}, 'position': {'x': 700, 'y': 1300}},
{'data': {'source': 'q14', 'target': 't142'}},
{'data': {'source': 't142', 'target': 't143'}},
{'data': {'source': 't143', 'target': 't144'}},
{'data': {'source': 't144', 'target': 'T14'}},
    #第15行
{'data': {'id': 'q15', 'label': '0','group': 'q'}, 'position': {'x': 0, 'y': 1400}},
{'data': {'id': 'E151','group': 'XE'}, 'position': {'x': 50, 'y': 1400}},
{'data': {'id': 't151','group': 't'}, 'position': {'x': 100, 'y': 1400}},
{'data': {'id': 'E152','group': 'E'}, 'position': {'x': 150, 'y': 1400}},
{'data': {'id': 't152','group': 't'}, 'position': {'x': 200, 'y': 1400}},
{'data': {'id': 'E153','group': 'XE'}, 'position': {'x': 250, 'y': 1400}},
{'data': {'id': 't153','group': 't'}, 'position': {'x': 300, 'y': 1400}},
{'data': {'id': 'E154','group': 'XE'}, 'position': {'x': 350, 'y': 1400}},
{'data': {'id': 't154','group': 't'}, 'position': {'x': 400, 'y': 1400}},
{'data': {'id': 'E155','group': 'XE'}, 'position': {'x': 450, 'y': 1400}},
{'data': {'id': 't155','group': 't'}, 'position': {'x': 500, 'y': 1400}},
{'data': {'id': 'E156','group': 'XE'}, 'position': {'x': 550, 'y': 1400}},
{'data': {'id': 'c15','group': 'c'}, 'position': {'x': 600, 'y': 1400}},
{'data': {'id': 'E157','group': 'nE'}, 'position': {'x': 650, 'y': 1400}},
{'data': {'id': 'T15','label': 'T','group': 'T'}, 'position': {'x': 700, 'y': 1400}},
{'data': {'source': 'q15', 'target': 't151'}},
{'data': {'source': 't151', 'target': 't152'}},
{'data': {'source': 't152', 'target': 't153'}},
{'data': {'source': 't153', 'target': 't154'}},
{'data': {'source': 't154', 'target': 't155'}},
{'data': {'source': 't155', 'target': 'c15'}},
{'data': {'source': 'c15', 'target': 'T15'}},

    #第16行
{'data': {'id': 'q16', 'label': '+','group': 'q'}, 'position': {'x': 0, 'y': 1500}},
{'data': {'id': 'E161','group': 'ZE'}, 'position': {'x': 50, 'y': 1500}},
{'data': {'id': 'c16','group': 'c'}, 'position': {'x': 100, 'y': 1500}},
{'data': {'id': 'E162','group': 'E'}, 'position': {'x': 150, 'y': 1500}},
{'data': {'id': 'qm', 'group': 'q'}, 'position': {'x': 700, 'y': 1500}},
{'data': {'source': 'q16', 'target': 'c16'}},
{'data': {'source': 'c16', 'target': 'qm'}},
]
CNOT1_edges =[{'data': {'source': 'c16', 'target': 't151'}},
              ]
CNOT2 = ['t92','t102','t112','t122','t132','t142','t152']  # 按需扩展
CNOT2_edges = [{'data': {'source': 'c8','target': target,}} for target in CNOT2]

CNOT3 = ['t53','t63','t73','t123','t133','t143','t153']  # 按需扩展
CNOT3_edges = [{'data': {'source': 'c4','target': target,}} for target in CNOT3]

CNOT4 = ['t34','t64','t74','t104','t114','t144','t154']  # 按需扩展
CNOT4_edges = [{'data': {'source': 'c2','target': target,}} for target in CNOT4]

CNOT5 = ['t35','t55','t75','t95','t115','t135','t155']  # 按需扩展
CNOT5_edges = [{'data': {'source': 'c1','target': target,}} for target in CNOT5]

CNOT6 = ['t36','t56','t66','t96','t106','t126']  # 按需扩展
CNOT6_edges = [{'data': {'source': 'c15','target': target,}} for target in CNOT6]
elements.extend(CNOT1_edges+CNOT2_edges+CNOT3_edges+CNOT4_edges+CNOT5_edges+CNOT6_edges)
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
            {'selector': 'node[group = "XE"]',  # X错误节点
             'style': {
                 'border-width': 1,  # 加粗矩形边框
                 'border-color': '#000000',  # 强制黑色边框
                 'background-color': '#FF0000',  # 保持原有白色填充
                 'shape': 'rectangle' , # 确保形状正确
                 'width': 25,  # 调整宽度以区分形状
                 'height': 25
             }},
            {'selector': 'node[group = "ZE"]',  # Z错误节点
             'style': {
                 'border-width': 1,  # 加粗矩形边框
                 'border-color': '#000000',  # 强制黑色边框
                 'background-color': '#0000FF',  # 保持原有白色填充
                 'shape': 'rectangle',  # 确保形状正确
                 'width': 25,  # 调整宽度以区分形状
                 'height': 25
             }},
            {'selector': 'node[group = "E"]',  # XZ错误节点
             'style': {
                 'border-width': 1,  # 加粗矩形边框
                 'border-color': '#000000',  # 强制黑色边框
                 'background-color': '#000000',  # 保持原有白色填充
                 'shape': 'rectangle',  # 确保形状正确
                 'width': 25,  # 调整宽度以区分形状
                 'height': 25
             }},
            {'selector': 'node[group = "nE"]',  # 无错误节点
             'style': {
                 'border-width': 1,  # 加粗矩形边框
                 'border-color': '#000000',  # 强制黑色边框
                 'background-color': '#FFFFFF',  # 保持原有白色填充
                 'shape': 'rectangle',  # 确保形状正确
                 'width': 25,  # 调整宽度以区分形状
                 'height': 25
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
            {'selector': 'node[group = "t"]',  # 目标节点
             'style': {
                 'border-width': 1,  # 加粗矩形边框
                 'border-color': '#000000',  # 强制黑色边框
                 'background-color': '#FFFFFF',  # 保持原有白色填充
                 'shape': 'ellipse',  # 确保形状正确
                 'width': 50,  # 调整宽度以区分形状
                 'height': 50
             }},
            {'selector': 'node[group = "T"]',  # T门节点
             'style': {
                 'border-width': 1,  # 加粗矩形边框
                 'border-color': '#000000',  # 强制黑色边框
                 'background-color': '#87CEFA',  # 保持原有白色填充
                 'shape': 'rectangle',  # 确保形状正确
                 'width': 50,  # 调整宽度以区分形状
                 'height': 50
             }},
        ]
    )
])
if __name__ == '__main__':
    TGpri.run(host='0.0.0.0', port=8051, debug=True)  # 必须设置host参数
