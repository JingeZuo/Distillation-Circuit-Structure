import dash
import dash_cytoscape as cyto
from dash import html
#%%
#15to1原始tanner graph
TGpri = dash.Dash(__name__)

elements = [
    #第一行X
    {'data': {'id': 'X11', 'label': 'X11','group': 'X'}, 'position': {'x': 0, 'y': 0}},
    {'data': {'id': 'CX112', 'label': 'CX112','group': 'C'}, 'position': {'x': 100, 'y': 0}},
    {'data': {'id': 'X12', 'label': 'X12','group': 'X'}, 'position': {'x': 200, 'y': 0}},
    {'data': {'id': 'CX123', 'label': 'CX123', 'group': 'C'}, 'position': {'x': 300, 'y': 0}},
    {'data': {'id': 'X13', 'label': 'X13', 'group': 'X'}, 'position': {'x': 400, 'y': 0}},
    {'data': {'id': 'CX134', 'label': 'CX134', 'group': 'C'}, 'position': {'x': 500, 'y': 0}},
    {'data': {'id': 'X14', 'label': 'X14', 'group': 'X'}, 'position': {'x': 600, 'y': 0}},
    {'data': {'id': 'CX145', 'label': 'CX145', 'group': 'C'}, 'position': {'x': 700, 'y': 0}},
    {'data': {'id': 'X15', 'label': 'X15', 'group': 'X'}, 'position': {'x': 800, 'y': 0}},
    {'data': {'id': 'CX156', 'label': 'CX156', 'group': 'C'}, 'position': {'x': 900, 'y': 0}},
    {'data': {'id': 'X16', 'label': 'X16', 'group': 'X'}, 'position': {'x': 1000, 'y': 0}},
    {'data': {'id': 'CX167', 'label': 'CX167', 'group': 'C'}, 'position': {'x': 1100, 'y': 0}},
    {'data': {'id': 'X17', 'label': 'X17', 'group': 'X'}, 'position': {'x': 1200, 'y': 0}},
    {'data': {'source': 'X12', 'target': 'CX123'}},
    {'data': {'source': 'X13', 'target': 'CX123'}},
    {'data': {'source': 'X13', 'target': 'CX134'}},
    {'data': {'source': 'X14', 'target': 'CX134'}},
    {'data': {'source': 'X14', 'target': 'CX145'}},
    {'data': {'source': 'X15', 'target': 'CX145'}},
    {'data': {'source': 'X15', 'target': 'CX156'}},
    {'data': {'source': 'X16', 'target': 'CX156'}},
    {'data': {'source': 'X16', 'target': 'CX167'}},
    {'data': {'source': 'X17', 'target': 'CX167'}},

    #第二行X
    {'data': {'id': 'X21', 'label': 'X21', 'group': 'X'}, 'position': {'x': 0, 'y': 100}},
    {'data': {'id': 'CX212', 'label': 'CX212', 'group': 'C'}, 'position': {'x': 100, 'y':100}},
    {'data': {'id': 'X22', 'label': 'X22', 'group': 'X'}, 'position': {'x': 200, 'y':100}},
    {'data': {'id': 'CX223', 'label': 'CX223', 'group': 'C'}, 'position': {'x': 300, 'y':100}},
    {'data': {'id': 'X23', 'label': 'X23', 'group': 'X'}, 'position': {'x': 400, 'y':100}},
    {'data': {'id': 'CX234', 'label': 'CX234', 'group': 'C'}, 'position': {'x': 500, 'y':100}},
    {'data': {'id': 'X24', 'label': 'X24', 'group': 'X'}, 'position': {'x': 600, 'y':100}},
    {'data': {'id': 'CX245', 'label': 'CX245', 'group': 'C'}, 'position': {'x': 700, 'y':100}},
    {'data': {'id': 'X25', 'label': 'X25', 'group': 'X'}, 'position': {'x': 800, 'y':100}},
    {'data': {'id': 'CX256', 'label': 'CX256', 'group': 'C'}, 'position': {'x': 900, 'y':100}},
    {'data': {'id': 'X26', 'label': 'X26', 'group': 'X'}, 'position': {'x': 1000, 'y':100}},
    {'data': {'id': 'CX267', 'label': 'CX267', 'group': 'C'}, 'position': {'x': 1100, 'y':100}},
    {'data': {'id': 'X27', 'label': 'X27', 'group': 'X'}, 'position': {'x': 1200, 'y':100}},
    {'data': {'source': 'X22', 'target': 'CX223'}},
    {'data': {'source': 'X23', 'target': 'CX223'}},
    {'data': {'source': 'X23', 'target': 'CX234'}},
    {'data': {'source': 'X24', 'target': 'CX234'}},
    {'data': {'source': 'X24', 'target': 'CX245'}},
    {'data': {'source': 'X25', 'target': 'CX245'}},
    {'data': {'source': 'X25', 'target': 'CX256'}},
    {'data': {'source': 'X26', 'target': 'CX256'}},
    {'data': {'source': 'X26', 'target': 'CX267'}},
    {'data': {'source': 'X27', 'target': 'CX267'}},
    # 第三行X
    {'data': {'id': 'X31', 'label': 'X31', 'group': 'X'}, 'position': {'x': 0, 'y': 200}},
    {'data': {'id': 'CX312', 'label': 'CX312', 'group': 'C'}, 'position': {'x': 100, 'y': 200}},
    {'data': {'id': 'X32', 'label': 'X32', 'group': 'X'}, 'position': {'x': 200, 'y': 200}},
    {'data': {'id': 'CX323', 'label': 'CX323', 'group': 'C'}, 'position': {'x': 300, 'y': 200}},
    {'data': {'id': 'X33', 'label': 'X33', 'group': 'X'}, 'position': {'x': 400, 'y': 200}},
    {'data': {'id': 'CX334', 'label': 'CX334', 'group': 'C'}, 'position': {'x': 500, 'y': 200}},
    {'data': {'id': 'X34', 'label': 'X34', 'group': 'X'}, 'position': {'x': 600, 'y': 200}},
    {'data': {'id': 'CX345', 'label': 'CX345', 'group': 'C'}, 'position': {'x': 700, 'y': 200}},
    {'data': {'id': 'X35', 'label': 'X35', 'group': 'X'}, 'position': {'x': 800, 'y': 200}},
    {'data': {'id': 'CX356', 'label': 'CX356', 'group': 'C'}, 'position': {'x': 900, 'y': 200}},
    {'data': {'id': 'X36', 'label': 'X36', 'group': 'X'}, 'position': {'x': 1000, 'y': 200}},
    {'data': {'id': 'CX367', 'label': 'CX367', 'group': 'C'}, 'position': {'x': 1100, 'y': 200}},
    {'data': {'id': 'X37', 'label': 'X37', 'group': 'X'}, 'position': {'x': 1200, 'y': 200}},
    {'data': {'source': 'X32', 'target': 'CX323'}},
    {'data': {'source': 'X33', 'target': 'CX323'}},
    {'data': {'source': 'X33', 'target': 'CX334'}},
    {'data': {'source': 'X34', 'target': 'CX334'}},
    {'data': {'source': 'X34', 'target': 'CX345'}},
    {'data': {'source': 'X35', 'target': 'CX345'}},
    {'data': {'source': 'X35', 'target': 'CX356'}},
    {'data': {'source': 'X36', 'target': 'CX356'}},
    {'data': {'source': 'X36', 'target': 'CX367'}},
    {'data': {'source': 'X37', 'target': 'CX367'}},

    # 第四行X
    {'data': {'id': 'X41', 'label': 'X41', 'group': 'X'}, 'position': {'x': 0, 'y': 300}},
    {'data': {'id': 'CX412', 'label': 'CX412', 'group': 'C'}, 'position': {'x': 100, 'y':300}},
    {'data': {'id': 'X42', 'label': 'X42', 'group': 'X'}, 'position': {'x': 200, 'y': 300}},
    {'data': {'id': 'CX423', 'label': 'CX423', 'group': 'C'}, 'position': {'x': 300, 'y': 300}},
    {'data': {'id': 'X43', 'label': 'X43', 'group': 'X'}, 'position': {'x': 400, 'y': 300}},
    {'data': {'id': 'CX434', 'label': 'CX434', 'group': 'C'}, 'position': {'x': 500, 'y': 300}},
    {'data': {'id': 'X44', 'label': 'X44', 'group': 'X'}, 'position': {'x': 600, 'y': 300}},
    {'data': {'id': 'CX445', 'label': 'CX445', 'group': 'C'}, 'position': {'x': 700, 'y': 300}},
    {'data': {'id': 'X45', 'label': 'X45', 'group': 'X'}, 'position': {'x': 800, 'y': 300}},
    {'data': {'id': 'CX456', 'label': 'CX456', 'group': 'C'}, 'position': {'x': 900, 'y': 300}},
    {'data': {'id': 'X46', 'label': 'X46', 'group': 'X'}, 'position': {'x': 1000, 'y': 300}},
    {'data': {'id': 'CX467', 'label': 'CX467', 'group': 'C'}, 'position': {'x': 1100, 'y': 300}},
    {'data': {'id': 'X47', 'label': 'X47', 'group': 'X'}, 'position': {'x': 1200, 'y': 300}},
    {'data': {'source': 'X42', 'target': 'CX412'}},
    {'data': {'source': 'X42', 'target': 'CX423'}},
    {'data': {'source': 'X43', 'target': 'CX423'}},
    {'data': {'source': 'X43', 'target': 'CX434'}},
    {'data': {'source': 'X44', 'target': 'CX434'}},
    {'data': {'source': 'X44', 'target': 'CX445'}},
    {'data': {'source': 'X45', 'target': 'CX445'}},
    {'data': {'source': 'X45', 'target': 'CX456'}},
    {'data': {'source': 'X46', 'target': 'CX456'}},
    {'data': {'source': 'X46', 'target': 'CX467'}},
    {'data': {'source': 'X47', 'target': 'CX467'}},

    # 第五行X
    {'data': {'id': 'X51', 'label': 'X51', 'group': 'X'}, 'position': {'x': 0, 'y': 400}},
    {'data': {'id': 'CX512', 'label': 'CX512', 'group': 'C'}, 'position': {'x': 100, 'y': 400}},
    {'data': {'id': 'X52', 'label': 'X52', 'group': 'X'}, 'position': {'x': 200, 'y': 400}},
    {'data': {'id': 'CX523', 'label': 'CX523', 'group': 'C'}, 'position': {'x': 300, 'y': 400}},
    {'data': {'id': 'X53', 'label': 'X53', 'group': 'X'}, 'position': {'x': 400, 'y': 400}},
    {'data': {'id': 'CX534', 'label': 'CX534', 'group': 'C'}, 'position': {'x': 500, 'y': 400}},
    {'data': {'id': 'X54', 'label': 'X54', 'group': 'X'}, 'position': {'x': 600, 'y': 400}},
    {'data': {'id': 'CX545', 'label': 'CX545', 'group': 'C'}, 'position': {'x': 700, 'y': 400}},
    {'data': {'id': 'X55', 'label': 'X55', 'group': 'X'}, 'position': {'x': 800, 'y': 400}},
    {'data': {'id': 'CX556', 'label': 'CX556', 'group': 'C'}, 'position': {'x': 900, 'y': 400}},
    {'data': {'id': 'X56', 'label': 'X56', 'group': 'X'}, 'position': {'x': 1000, 'y': 400}},
    {'data': {'id': 'CX567', 'label': 'CX567', 'group': 'C'}, 'position': {'x': 1100, 'y': 400}},
    {'data': {'id': 'X57', 'label': 'X57', 'group': 'X'}, 'position': {'x': 1200, 'y': 400}},
    {'data': {'source': 'X52', 'target': 'CX512'}},
    {'data': {'source': 'X52', 'target': 'CX523'}},
    {'data': {'source': 'X53', 'target': 'CX523'}},
    {'data': {'source': 'X53', 'target': 'CX534'}},
    {'data': {'source': 'X54', 'target': 'CX534'}},
    {'data': {'source': 'X54', 'target': 'CX545'}},
    {'data': {'source': 'X55', 'target': 'CX545'}},
    {'data': {'source': 'X55', 'target': 'CX556'}},
    {'data': {'source': 'X56', 'target': 'CX556'}},
    {'data': {'source': 'X56', 'target': 'CX567'}},
    {'data': {'source': 'X57', 'target': 'CX567'}},

    # 第六行X
    {'data': {'id': 'X61', 'label': 'X61', 'group': 'X'}, 'position': {'x': 0, 'y': 500}},
    {'data': {'id': 'CX612', 'label': 'CX612', 'group': 'C'}, 'position': {'x': 100, 'y': 500}},
    {'data': {'id': 'X62', 'label': 'X62', 'group': 'X'}, 'position': {'x': 200, 'y': 500}},
    {'data': {'id': 'CX623', 'label': 'CX623', 'group': 'C'}, 'position': {'x': 300, 'y': 500}},
    {'data': {'id': 'X63', 'label': 'X63', 'group': 'X'}, 'position': {'x': 400, 'y': 500}},
    {'data': {'id': 'CX634', 'label': 'CX634', 'group': 'C'}, 'position': {'x': 500, 'y': 500}},
    {'data': {'id': 'X64', 'label': 'X64', 'group': 'X'}, 'position': {'x': 600, 'y': 500}},
    {'data': {'id': 'CX645', 'label': 'CX645', 'group': 'C'}, 'position': {'x': 700, 'y': 500}},
    {'data': {'id': 'X65', 'label': 'X65', 'group': 'X'}, 'position': {'x': 800, 'y': 500}},
    {'data': {'id': 'CX656', 'label': 'CX656', 'group': 'C'}, 'position': {'x': 900, 'y': 500}},
    {'data': {'id': 'X66', 'label': 'X66', 'group': 'X'}, 'position': {'x': 1000, 'y': 500}},
    {'data': {'id': 'CX667', 'label': 'CX667', 'group': 'C'}, 'position': {'x': 1100, 'y': 500}},
    {'data': {'id': 'X67', 'label': 'X67', 'group': 'X'}, 'position': {'x': 1200, 'y': 500}},
    {'data': {'source': 'X62', 'target': 'CX623'}},
    {'data': {'source': 'X63', 'target': 'CX623'}},
    {'data': {'source': 'X63', 'target': 'CX634'}},
    {'data': {'source': 'X64', 'target': 'CX634'}},
    {'data': {'source': 'X64', 'target': 'CX645'}},
    {'data': {'source': 'X65', 'target': 'CX645'}},
    {'data': {'source': 'X65', 'target': 'CX656'}},
    {'data': {'source': 'X66', 'target': 'CX656'}},
    {'data': {'source': 'X66', 'target': 'CX667'}},
    {'data': {'source': 'X67', 'target': 'CX667'}},
    {'data': {'source': 'X62', 'target': 'CX612'}},

    # 第七行X
    {'data': {'id': 'X71', 'label': 'X71', 'group': 'X'}, 'position': {'x': 0, 'y': 600}},
    {'data': {'id': 'CX712', 'label': 'CX712', 'group': 'C'}, 'position': {'x': 100, 'y': 600}},
    {'data': {'id': 'X72', 'label': 'X72', 'group': 'X'}, 'position': {'x': 200, 'y': 600}},
    {'data': {'id': 'CX723', 'label': 'CX723', 'group': 'C'}, 'position': {'x': 300, 'y': 600}},
    {'data': {'id': 'X73', 'label': 'X73', 'group': 'X'}, 'position': {'x': 400, 'y': 600}},
    {'data': {'id': 'CX734', 'label': 'CX734', 'group': 'C'}, 'position': {'x': 500, 'y': 600}},
    {'data': {'id': 'X74', 'label': 'X74', 'group': 'X'}, 'position': {'x': 600, 'y': 600}},
    {'data': {'id': 'CX745', 'label': 'CX745', 'group': 'C'}, 'position': {'x': 700, 'y': 600}},
    {'data': {'id': 'X75', 'label': 'X75', 'group': 'X'}, 'position': {'x': 800, 'y': 600}},
    {'data': {'id': 'CX756', 'label': 'CX756', 'group': 'C'}, 'position': {'x': 900, 'y': 600}},
    {'data': {'id': 'X76', 'label': 'X76', 'group': 'X'}, 'position': {'x': 1000, 'y': 600}},
    {'data': {'id': 'CX767', 'label': 'CX767', 'group': 'C'}, 'position': {'x': 1100, 'y': 600}},
    {'data': {'id': 'X77', 'label': 'X77', 'group': 'X'}, 'position': {'x': 1200, 'y': 600}},
    {'data': {'source': 'X72', 'target': 'CX723'}},
    {'data': {'source': 'X73', 'target': 'CX723'}},
    {'data': {'source': 'X73', 'target': 'CX734'}},
    {'data': {'source': 'X74', 'target': 'CX734'}},
    {'data': {'source': 'X74', 'target': 'CX745'}},
    {'data': {'source': 'X75', 'target': 'CX745'}},
    {'data': {'source': 'X75', 'target': 'CX756'}},
    {'data': {'source': 'X76', 'target': 'CX756'}},
    {'data': {'source': 'X76', 'target': 'CX767'}},
    {'data': {'source': 'X77', 'target': 'CX767'}},
    {'data': {'source': 'X72', 'target': 'CX712'}},

    # 第八行X
    {'data': {'id': 'X81', 'label': 'X81', 'group': 'X'}, 'position': {'x': 0, 'y':700}},
    {'data': {'id': 'CX812', 'label': 'CX812', 'group': 'C'}, 'position': {'x': 100, 'y':700}},
    {'data': {'id': 'X82', 'label': 'X82', 'group': 'X'}, 'position': {'x': 200, 'y':700}},
    {'data': {'id': 'CX823', 'label': 'CX823', 'group': 'C'}, 'position': {'x': 300, 'y': 700}},
    {'data': {'id': 'X83', 'label': 'X83', 'group': 'X'}, 'position': {'x': 400, 'y':700}},
    {'data': {'id': 'CX834', 'label': 'CX834', 'group': 'C'}, 'position': {'x': 500, 'y':700}},
    {'data': {'id': 'X84', 'label': 'X84', 'group': 'X'}, 'position': {'x': 600, 'y':700}},
    {'data': {'id': 'CX845', 'label': 'CX845', 'group': 'C'}, 'position': {'x': 700, 'y':700}},
    {'data': {'id': 'X85', 'label': 'X85', 'group': 'X'}, 'position': {'x': 800, 'y':700}},
    {'data': {'id': 'CX856', 'label': 'CX856', 'group': 'C'}, 'position': {'x': 900, 'y':700}},
    {'data': {'id': 'X86', 'label': 'X86', 'group': 'X'}, 'position': {'x': 1000, 'y':700}},
    {'data': {'id': 'CX867', 'label': 'CX867', 'group': 'C'}, 'position': {'x': 1100, 'y':700}},
    {'data': {'id': 'X87', 'label': 'X87', 'group': 'X'}, 'position': {'x': 1200, 'y':700}},
    {'data': {'source': 'X82', 'target': 'CX823'}},
    {'data': {'source': 'X83', 'target': 'CX823'}},
    {'data': {'source': 'X83', 'target': 'CX834'}},
    {'data': {'source': 'X84', 'target': 'CX834'}},
    {'data': {'source': 'X84', 'target': 'CX845'}},
    {'data': {'source': 'X85', 'target': 'CX845'}},
    {'data': {'source': 'X85', 'target': 'CX856'}},
    {'data': {'source': 'X86', 'target': 'CX856'}},
    {'data': {'source': 'X86', 'target': 'CX867'}},
    {'data': {'source': 'X87', 'target': 'CX867'}},


    # 第1行Z
    {'data': {'id': 'Z11', 'label': 'Z11', 'group': 'Z'}, 'position': {'x': 1800, 'y': 0}},
    {'data': {'id': 'CZ112', 'label': 'CZ112', 'group': 'C'}, 'position': {'x': 1900, 'y': 0}},
    {'data': {'id': 'Z12', 'label': 'Z12', 'group': 'Z'}, 'position': {'x': 2000, 'y': 0}},
    {'data': {'id': 'CZ123', 'label': 'CZ123', 'group': 'C'}, 'position': {'x': 2100, 'y': 0}},
    {'data': {'id': 'Z13', 'label': 'Z13', 'group': 'Z'}, 'position': {'x': 2200, 'y': 0}},
    {'data': {'id': 'CZ134', 'label': 'CZ134', 'group': 'C'}, 'position': {'x': 2300, 'y': 0}},
    {'data': {'id': 'Z14', 'label': 'Z14', 'group': 'Z'}, 'position': {'x': 2400, 'y': 0}},
    {'data': {'id': 'CZ145', 'label': 'CZ145', 'group': 'C'}, 'position': {'x': 2500, 'y': 0}},
    {'data': {'id': 'Z15', 'label': 'Z15', 'group': 'Z'}, 'position': {'x': 2600, 'y': 0}},
    {'data': {'id': 'CZ156', 'label': 'CZ156', 'group': 'C'}, 'position': {'x': 2700, 'y': 0}},
    {'data': {'id': 'Z16', 'label': 'Z16', 'group': 'Z'}, 'position': {'x': 2800, 'y': 0}},
    {'data': {'id': 'CZ167', 'label': 'CZ167', 'group': 'C'}, 'position': {'x': 2900, 'y': 0}},
    {'data': {'id': 'Z17', 'label': 'Z17', 'group': 'Z'}, 'position': {'x': 3000, 'y': 0}},
    {'data': {'source': 'Z12', 'target': 'CZ123'}},
    {'data': {'source': 'Z13', 'target': 'CZ123'}},
    {'data': {'source': 'Z13', 'target': 'CZ134'}},
    {'data': {'source': 'Z14', 'target': 'CZ134'}},
    {'data': {'source': 'Z14', 'target': 'CZ145'}},
    {'data': {'source': 'Z15', 'target': 'CZ145'}},
    {'data': {'source': 'Z15', 'target': 'CZ156'}},
    {'data': {'source': 'Z16', 'target': 'CZ156'}},
    {'data': {'source': 'Z16', 'target': 'CZ167'}},
    {'data': {'source': 'Z17', 'target': 'CZ167'}},
    {'data': {'source': 'Z12', 'target': 'CZ112'}},

    #第2行Z
    {'data': {'id': 'Z21', 'label': 'Z21', 'group': 'Z'}, 'position': {'x': 1800, 'y': 100}},
    {'data': {'id': 'CZ212', 'label': 'CZ212','group': 'C'}, 'position': {'x': 1900, 'y': 100}},
    {'data': {'id': 'Z22', 'label': 'Z22', 'group': 'Z'}, 'position': {'x': 2000, 'y': 100}},
    {'data': {'id': 'CZ223', 'label': 'CZ223', 'group': 'C'}, 'position': {'x': 2100, 'y': 100}},
    {'data': {'id': 'Z23', 'label': 'Z23', 'group': 'Z'}, 'position': {'x': 2200, 'y': 100}},
    {'data': {'id': 'CZ234', 'label': 'CZ234', 'group': 'C'}, 'position': {'x': 2300, 'y': 100}},
    {'data': {'id': 'Z24', 'label': 'Z24', 'group': 'Z'}, 'position': {'x': 2400, 'y': 100}},
    {'data': {'id': 'CZ245', 'label': 'CZ245', 'group': 'C'}, 'position': {'x': 2500, 'y': 100}},
    {'data': {'id': 'Z25', 'label': 'Z25', 'group': 'Z'}, 'position': {'x': 2600, 'y': 100}},
    {'data': {'id': 'CZ256', 'label': 'CZ256', 'group': 'C'}, 'position': {'x': 2700, 'y': 100}},
    {'data': {'id': 'Z26', 'label': 'Z26', 'group': 'Z'}, 'position': {'x': 2800, 'y': 100}},
    {'data': {'id': 'CZ267', 'label': 'CZ267', 'group': 'C'}, 'position': {'x': 2900, 'y': 100}},
    {'data': {'id': 'Z27', 'label': 'Z27', 'group': 'Z'}, 'position': {'x': 3000, 'y': 100}},
    {'data': {'source': 'Z22', 'target': 'CZ223'}},
    {'data': {'source': 'Z23', 'target': 'CZ223'}},
    {'data': {'source': 'Z23', 'target': 'CZ234'}},
    {'data': {'source': 'Z24', 'target': 'CZ234'}},
    {'data': {'source': 'Z24', 'target': 'CZ245'}},
    {'data': {'source': 'Z25', 'target': 'CZ245'}},
    {'data': {'source': 'Z25', 'target': 'CZ256'}},
    {'data': {'source': 'Z26', 'target': 'CZ256'}},
    {'data': {'source': 'Z26', 'target': 'CZ267'}},
    {'data': {'source': 'Z27', 'target': 'CZ267'}},
    {'data': {'source': 'Z22', 'target': 'CZ212'}},

    # 第3行Z
    {'data': {'id': 'Z31', 'label': 'Z31', 'group': 'Z'}, 'position': {'x': 1800, 'y': 200}},
    {'data': {'id': 'CZ312', 'label': 'CZ312', 'group': 'C'}, 'position': {'x': 1900, 'y': 200}},
    {'data': {'id': 'Z32', 'label': 'Z32', 'group': 'Z'}, 'position': {'x': 2000, 'y': 200}},
    {'data': {'id': 'CZ323', 'label': 'CZ323', 'group': 'C'}, 'position': {'x': 2100, 'y': 200}},
    {'data': {'id': 'Z33', 'label': 'Z33', 'group': 'Z'}, 'position': {'x': 2200, 'y': 200}},
    {'data': {'id': 'CZ334', 'label': 'CZ334', 'group': 'C'}, 'position': {'x': 2300, 'y': 200}},
    {'data': {'id': 'Z34', 'label': 'Z34', 'group': 'Z'}, 'position': {'x': 2400, 'y': 200}},
    {'data': {'id': 'CZ345', 'label': 'CZ345', 'group': 'C'}, 'position': {'x': 2500, 'y': 200}},
    {'data': {'id': 'Z35', 'label': 'Z35', 'group': 'Z'}, 'position': {'x': 2600, 'y': 200}},
    {'data': {'id': 'CZ356', 'label': 'CZ356', 'group': 'C'}, 'position': {'x': 2700, 'y': 200}},
    {'data': {'id': 'Z36', 'label': 'Z36', 'group': 'Z'}, 'position': {'x': 2800, 'y': 200}},
    {'data': {'id': 'CZ367', 'label': 'CZ367', 'group': 'C'}, 'position': {'x': 2900, 'y': 200}},
    {'data': {'id': 'Z37', 'label': 'Z37', 'group': 'Z'}, 'position': {'x': 3000, 'y': 200}},
    {'data': {'source': 'Z32', 'target': 'CZ312'}},
    {'data': {'source': 'Z32', 'target': 'CZ323'}},
    {'data': {'source': 'Z33', 'target': 'CZ323'}},
    {'data': {'source': 'Z33', 'target': 'CZ334'}},
    {'data': {'source': 'Z34', 'target': 'CZ334'}},
    {'data': {'source': 'Z34', 'target': 'CZ345'}},
    {'data': {'source': 'Z35', 'target': 'CZ345'}},
    {'data': {'source': 'Z35', 'target': 'CZ356'}},
    {'data': {'source': 'Z36', 'target': 'CZ356'}},
    {'data': {'source': 'Z36', 'target': 'CZ367'}},
    {'data': {'source': 'Z37', 'target': 'CZ367'}},

    # 第4行Z
    {'data': {'id': 'Z41', 'label': 'Z41', 'group': 'Z'}, 'position': {'x': 1800, 'y': 300}},
    {'data': {'id': 'CZ412', 'label': 'CZ412', 'group': 'C'}, 'position': {'x': 1900, 'y': 300}},
    {'data': {'id': 'Z42', 'label': 'Z42', 'group': 'Z'}, 'position': {'x': 2000, 'y': 300}},
    {'data': {'id': 'CZ423', 'label': 'CZ423', 'group': 'C'}, 'position': {'x': 2100, 'y': 300}},
    {'data': {'id': 'Z43', 'label': 'Z43', 'group': 'Z'}, 'position': {'x': 2200, 'y': 300}},
    {'data': {'id': 'CZ434', 'label': 'CZ434', 'group': 'C'}, 'position': {'x': 2300, 'y': 300}},
    {'data': {'id': 'Z44', 'label': 'Z44', 'group': 'Z'}, 'position': {'x': 2400, 'y': 300}},
    {'data': {'id': 'CZ445', 'label': 'CZ445', 'group': 'C'}, 'position': {'x': 2500, 'y': 300}},
    {'data': {'id': 'Z45', 'label': 'Z45', 'group': 'Z'}, 'position': {'x': 2600, 'y': 300}},
    {'data': {'id': 'CZ456', 'label': 'CZ456', 'group': 'C'}, 'position': {'x': 2700, 'y': 300}},
    {'data': {'id': 'Z46', 'label': 'Z46', 'group': 'Z'}, 'position': {'x': 2800, 'y': 300}},
    {'data': {'id': 'CZ467', 'label': 'CZ467', 'group': 'C'}, 'position': {'x': 2900, 'y': 300}},
    {'data': {'id': 'Z47', 'label': 'Z47', 'group': 'Z'}, 'position': {'x': 3000, 'y': 300}},
    {'data': {'source': 'Z42', 'target': 'CZ423'}},
    {'data': {'source': 'Z43', 'target': 'CZ423'}},
    {'data': {'source': 'Z43', 'target': 'CZ434'}},
    {'data': {'source': 'Z44', 'target': 'CZ434'}},
    {'data': {'source': 'Z44', 'target': 'CZ445'}},
    {'data': {'source': 'Z45', 'target': 'CZ445'}},
    {'data': {'source': 'Z45', 'target': 'CZ456'}},
    {'data': {'source': 'Z46', 'target': 'CZ456'}},
    {'data': {'source': 'Z46', 'target': 'CZ467'}},
    {'data': {'source': 'Z47', 'target': 'CZ467'}},

    # 第5行Z
    {'data': {'id': 'Z51', 'label': 'Z51', 'group': 'Z'}, 'position': {'x': 1800, 'y': 400}},
    {'data': {'id': 'CZ512', 'label': 'CZ512', 'group': 'C'}, 'position': {'x': 1900, 'y': 400}},
    {'data': {'id': 'Z52', 'label': 'Z52', 'group': 'Z'}, 'position': {'x': 2000, 'y': 400}},
    {'data': {'id': 'CZ523', 'label': 'CZ523', 'group': 'C'}, 'position': {'x': 2100, 'y': 400}},
    {'data': {'id': 'Z53', 'label': 'Z53', 'group': 'Z'}, 'position': {'x': 2200, 'y': 400}},
    {'data': {'id': 'CZ534', 'label': 'CZ534', 'group': 'C'}, 'position': {'x': 2300, 'y': 400}},
    {'data': {'id': 'Z54', 'label': 'Z54', 'group': 'Z'}, 'position': {'x': 2400, 'y': 400}},
    {'data': {'id': 'CZ545', 'label': 'CZ545', 'group': 'C'}, 'position': {'x': 2500, 'y': 400}},
    {'data': {'id': 'Z55', 'label': 'Z55', 'group': 'Z'}, 'position': {'x': 2600, 'y': 400}},
    {'data': {'id': 'CZ556', 'label': 'CZ556', 'group': 'C'}, 'position': {'x': 2700, 'y': 400}},
    {'data': {'id': 'Z56', 'label': 'Z56', 'group': 'Z'}, 'position': {'x': 2800, 'y': 400}},
    {'data': {'id': 'CZ567', 'label': 'CZ567', 'group': 'C'}, 'position': {'x': 2900, 'y': 400}},
    {'data': {'id': 'Z57', 'label': 'Z57', 'group': 'Z'}, 'position': {'x': 3000, 'y': 400}},
    {'data': {'source': 'Z52', 'target': 'CZ523'}},
    {'data': {'source': 'Z53', 'target': 'CZ523'}},
    {'data': {'source': 'Z53', 'target': 'CZ534'}},
    {'data': {'source': 'Z54', 'target': 'CZ534'}},
    {'data': {'source': 'Z54', 'target': 'CZ545'}},
    {'data': {'source': 'Z55', 'target': 'CZ545'}},
    {'data': {'source': 'Z55', 'target': 'CZ556'}},
    {'data': {'source': 'Z56', 'target': 'CZ556'}},
    {'data': {'source': 'Z56', 'target': 'CZ567'}},
    {'data': {'source': 'Z57', 'target': 'CZ567'}},

    # 第6行Z
    {'data': {'id': 'Z61', 'label': 'Z61', 'group': 'Z'}, 'position': {'x': 1800, 'y': 500}},
    {'data': {'id': 'CZ612', 'label': 'CZ612', 'group': 'C'}, 'position': {'x': 1900, 'y': 500}},
    {'data': {'id': 'Z62', 'label': 'Z62', 'group': 'Z'}, 'position': {'x': 2000, 'y': 500}},
    {'data': {'id': 'CZ623', 'label': 'CZ623', 'group': 'C'}, 'position': {'x': 2100, 'y': 500}},
    {'data': {'id': 'Z63', 'label': 'Z63', 'group': 'Z'}, 'position': {'x': 2200, 'y': 500}},
    {'data': {'id': 'CZ634', 'label': 'CZ634', 'group': 'C'}, 'position': {'x': 2300, 'y': 500}},
    {'data': {'id': 'Z64', 'label': 'Z64', 'group': 'Z'}, 'position': {'x': 2400, 'y': 500}},
    {'data': {'id': 'CZ645', 'label': 'CZ645', 'group': 'C'}, 'position': {'x': 2500, 'y': 500}},
    {'data': {'id': 'Z65', 'label': 'Z65', 'group': 'Z'}, 'position': {'x': 2600, 'y': 500}},
    {'data': {'id': 'CZ656', 'label': 'CZ656', 'group': 'C'}, 'position': {'x': 2700, 'y': 500}},
    {'data': {'id': 'Z66', 'label': 'Z66', 'group': 'Z'}, 'position': {'x': 2800, 'y': 500}},
    {'data': {'id': 'CZ667', 'label': 'CZ667', 'group': 'C'}, 'position': {'x': 2900, 'y': 500}},
    {'data': {'id': 'Z67', 'label': 'Z67', 'group': 'Z'}, 'position': {'x': 3000, 'y': 500}},
    {'data': {'source': 'Z62', 'target': 'CZ623'}},
    {'data': {'source': 'Z63', 'target': 'CZ623'}},
    {'data': {'source': 'Z63', 'target': 'CZ634'}},
    {'data': {'source': 'Z64', 'target': 'CZ634'}},
    {'data': {'source': 'Z64', 'target': 'CZ645'}},
    {'data': {'source': 'Z65', 'target': 'CZ645'}},
    {'data': {'source': 'Z65', 'target': 'CZ656'}},
    {'data': {'source': 'Z66', 'target': 'CZ656'}},
    {'data': {'source': 'Z66', 'target': 'CZ667'}},
    {'data': {'source': 'Z67', 'target': 'CZ667'}},

    # 第7行Z
    {'data': {'id': 'Z71', 'label': 'Z71', 'group': 'Z'}, 'position': {'x': 1800, 'y': 600}},
    {'data': {'id': 'CZ712', 'label': 'CZ712', 'group': 'C'}, 'position': {'x': 1900, 'y': 600}},
    {'data': {'id': 'Z72', 'label': 'Z72', 'group': 'Z'}, 'position': {'x': 2000, 'y': 600}},
    {'data': {'id': 'CZ723', 'label': 'CZ723', 'group': 'C'}, 'position': {'x': 2100, 'y': 600}},
    {'data': {'id': 'Z73', 'label': 'Z73', 'group': 'Z'}, 'position': {'x': 2200, 'y': 600}},
    {'data': {'id': 'CZ734', 'label': 'CZ734', 'group': 'C'}, 'position': {'x': 2300, 'y': 600}},
    {'data': {'id': 'Z74', 'label': 'Z74', 'group': 'Z'}, 'position': {'x': 2400, 'y': 600}},
    {'data': {'id': 'CZ745', 'label': 'CZ745', 'group': 'C'}, 'position': {'x': 2500, 'y': 600}},
    {'data': {'id': 'Z75', 'label': 'Z75', 'group': 'Z'}, 'position': {'x': 2600, 'y': 600}},
    {'data': {'id': 'CZ756', 'label': 'CZ756', 'group': 'C'}, 'position': {'x': 2700, 'y': 600}},
    {'data': {'id': 'Z76', 'label': 'Z76', 'group': 'Z'}, 'position': {'x': 2800, 'y': 600}},
    {'data': {'id': 'CZ767', 'label': 'CZ767', 'group': 'C'}, 'position': {'x': 2900, 'y': 600}},
    {'data': {'id': 'Z77', 'label': 'Z77', 'group': 'Z'}, 'position': {'x': 3000, 'y': 600}},
    {'data': {'source': 'Z72', 'target': 'CZ723'}},
    {'data': {'source': 'Z73', 'target': 'CZ723'}},
    {'data': {'source': 'Z73', 'target': 'CZ734'}},
    {'data': {'source': 'Z74', 'target': 'CZ734'}},
    {'data': {'source': 'Z74', 'target': 'CZ745'}},
    {'data': {'source': 'Z75', 'target': 'CZ745'}},
    {'data': {'source': 'Z75', 'target': 'CZ756'}},
    {'data': {'source': 'Z76', 'target': 'CZ756'}},
    {'data': {'source': 'Z76', 'target': 'CZ767'}},
    {'data': {'source': 'Z77', 'target': 'CZ767'}},

    # 第8行Z
    {'data': {'id': 'Z81', 'label': 'Z81', 'group': 'Z'}, 'position': {'x': 1800, 'y': 700}},
    {'data': {'id': 'CZ812', 'label': 'CZ812', 'group': 'C'}, 'position': {'x': 1900, 'y': 700}},
    {'data': {'id': 'Z82', 'label': 'Z82', 'group': 'Z'}, 'position': {'x': 2000, 'y': 700}},
    {'data': {'id': 'CZ823', 'label': 'CZ823', 'group': 'C'}, 'position': {'x': 2100, 'y': 700}},
    {'data': {'id': 'Z83', 'label': 'Z83', 'group': 'Z'}, 'position': {'x': 2200, 'y': 700}},
    {'data': {'id': 'CZ834', 'label': 'CZ834', 'group': 'C'}, 'position': {'x': 2300, 'y': 700}},
    {'data': {'id': 'Z84', 'label': 'Z84', 'group': 'Z'}, 'position': {'x': 2400, 'y': 700}},
    {'data': {'id': 'CZ845', 'label': 'CZ845', 'group': 'C'}, 'position': {'x': 2500, 'y': 700}},
    {'data': {'id': 'Z85', 'label': 'Z85', 'group': 'Z'}, 'position': {'x': 2600, 'y': 700}},
    {'data': {'id': 'CZ856', 'label': 'CZ856', 'group': 'C'}, 'position': {'x': 2700, 'y': 700}},
    {'data': {'id': 'Z86', 'label': 'Z86', 'group': 'Z'}, 'position': {'x': 2800, 'y': 700}},
    {'data': {'id': 'CZ867', 'label': 'CZ867', 'group': 'C'}, 'position': {'x': 2900, 'y': 700}},
    {'data': {'id': 'Z87', 'label': 'Z87', 'group': 'Z'}, 'position': {'x': 3000, 'y': 700}},
    {'data': {'source': 'Z82', 'target': 'CZ823'}},
    {'data': {'source': 'Z83', 'target': 'CZ823'}},
    {'data': {'source': 'Z83', 'target': 'CZ834'}},
    {'data': {'source': 'Z84', 'target': 'CZ834'}},
    {'data': {'source': 'Z84', 'target': 'CZ845'}},
    {'data': {'source': 'Z85', 'target': 'CZ845'}},
    {'data': {'source': 'Z85', 'target': 'CZ856'}},
    {'data': {'source': 'Z86', 'target': 'CZ856'}},
    {'data': {'source': 'Z86', 'target': 'CZ867'}},
    {'data': {'source': 'Z87', 'target': 'CZ867'}},
    {'data': {'source': 'Z82', 'target': 'CZ812'}},


]
CNOT1_edges =[{'data': {'source': 'X82', 'target': 'CX723'}},
              {'data': {'source': 'Z72', 'target': 'CZ823'}},]

CNOT2X = ['CX434', 'CX534']  # 按需扩展
CNOT2X_edges = [{'data': {'source': 'X73','target': target,}} for target in CNOT2X]
CNOT2Z = ['Z43', 'Z53']
CNOT2Z_edges = [{'data': {'source': 'CZ734','target': target,}} for target in CNOT2Z]

CNOT3X = ['CX445', 'CX545', 'CX645']  # 按需扩展
CNOT3X_edges = [{'data': {'source': 'X34','target': target,}} for target in CNOT3X]
CNOT3Z = ['Z44', 'Z54', 'Z64']
CNOT3Z_edges = [{'data': {'source': 'CZ345','target': target,}} for target in CNOT3Z]

CNOT4X = ['CX556', 'CX656', 'CX756']  # 按需扩展
CNOT4X_edges = [{'data': {'source': 'X25','target': target,}} for target in CNOT4X]
CNOT4Z = ['Z55', 'Z65', 'Z75']
CNOT4Z_edges = [{'data': {'source': 'CZ256','target': target,}} for target in CNOT4Z]

CNOT5X = ['CX467', 'CX667', 'CX767']  # 按需扩展
CNOT5X_edges = [{'data': {'source': 'X16','target': target,}} for target in CNOT5X]
CNOT5Z = ['Z46', 'Z66', 'Z76']
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
