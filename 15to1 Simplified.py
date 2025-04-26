import dash
import dash_cytoscape as cyto
from dash import html
#%%
TGDeiso = dash.Dash(__name__)

elements = [
    #第一行X
    {'data': {'id': 'X15', 'label': 'X15', 'group': 'X'}, 'position': {'x': 900, 'y': 0}},
    {'data': {'id': 'CX178', 'label': 'CX178', 'group': 'C'}, 'position': {'x': 1400, 'y': 0}},
    {'data': {'id': 'X18', 'label': 'X18', 'group': 'X'}, 'position': {'x': 1500, 'y': 0}},
    {'data': {'source': 'X15', 'target': 'CX178'}},
    {'data': {'source': 'X18', 'target': 'CX178'}},

    #第二行X
    {'data': {'id': 'X24', 'label': 'X24', 'group': 'X'}, 'position': {'x': 700, 'y':100}},
    {'data': {'id': 'CX278', 'label': 'CX278', 'group': 'C'}, 'position': {'x': 1400, 'y':100}},
    {'data': {'id': 'X28', 'label': 'X28', 'group': 'X'}, 'position': {'x': 1500, 'y':100}},
    {'data': {'source': 'X24', 'target': 'CX278'}},
    {'data': {'source': 'X28', 'target': 'CX278'}},

    # 第三行X
    {'data': {'id': 'CX367', 'label': 'CX367', 'group': 'C'}, 'position': {'x': 1200, 'y': 200}},
    {'data': {'id': 'X37', 'label': 'X37', 'group': 'X'}, 'position': {'x': 1300, 'y': 200}},
    {'data': {'id': 'CX378', 'label': 'CX378', 'group': 'C'}, 'position': {'x': 1400, 'y': 200}},
    {'data': {'id': 'X38', 'label': 'X38', 'group': 'X'}, 'position': {'x': 1500, 'y': 200}},
    {'data': {'source': 'X37', 'target': 'CX367'}},
    {'data': {'source': 'X37', 'target': 'CX378'}},
    {'data': {'source': 'X38', 'target': 'CX378'}},

    # 第四行X
    {'data': {'id': 'X43', 'label': 'X43', 'group': 'X'}, 'position': {'x': 500, 'y': 300}},
    {'data': {'id': 'CX478', 'label': 'CX478', 'group': 'C'}, 'position': {'x': 1400, 'y': 300}},
    {'data': {'id': 'X48', 'label': 'X48', 'group': 'X'}, 'position': {'x': 1500, 'y': 300}},
    {'data': {'source': 'X43', 'target': 'CX478'}},
    {'data': {'source': 'X48', 'target': 'CX478'}},

    # 第五行X
    {'data': {'id': 'CX567', 'label': 'CX567', 'group': 'C'}, 'position': {'x': 1200, 'y': 400}},
    {'data': {'id': 'X57', 'label': 'X57', 'group': 'X'}, 'position': {'x': 1300, 'y': 400}},
    {'data': {'id': 'CX578', 'label': 'CX578', 'group': 'C'}, 'position': {'x': 1400, 'y': 400}},
    {'data': {'id': 'X58', 'label': 'X58', 'group': 'X'}, 'position': {'x': 1500, 'y': 400}},
    {'data': {'source': 'X57', 'target': 'CX567'}},
    {'data': {'source': 'X57', 'target': 'CX578'}},
    {'data': {'source': 'X58', 'target': 'CX578'}},

    # 第六行X
    {'data': {'id': 'CX667', 'label': 'CX667', 'group': 'C'}, 'position': {'x': 1200, 'y': 500}},
    {'data': {'id': 'X67', 'label': 'X67', 'group': 'X'}, 'position': {'x': 1300, 'y': 500}},
    {'data': {'id': 'CX678', 'label': 'CX678', 'group': 'C'}, 'position': {'x': 1400, 'y': 500}},
    {'data': {'id': 'X68', 'label': 'X68', 'group': 'X'}, 'position': {'x': 1500, 'y': 500}},
    {'data': {'source': 'X67', 'target': 'CX667'}},
    {'data': {'source': 'X67', 'target': 'CX678'}},
    {'data': {'source': 'X68', 'target': 'CX678'}},

    # 第七行X
    {'data': {'id': 'CX756', 'label': 'CX756', 'group': 'C'}, 'position': {'x': 1000, 'y': 600}},
    {'data': {'id': 'X77', 'label': 'X77', 'group': 'X'}, 'position': {'x': 1300, 'y': 600}},
    {'data': {'id': 'CX778', 'label': 'CX778', 'group': 'C'}, 'position': {'x': 1400, 'y': 600}},
    {'data': {'id': 'X78', 'label': 'X78', 'group': 'X'}, 'position': {'x': 1500, 'y': 600}},
    {'data': {'source': 'X77', 'target': 'CX756'}},
    {'data': {'source': 'X77', 'target': 'CX778'}},
    {'data': {'source': 'X78', 'target': 'CX778'}},

    # 第八行X
    {'data': {'id': 'X82', 'label': 'X82', 'group': 'X'}, 'position': {'x': 300, 'y':700}},
    {'data': {'id': 'CX878', 'label': 'CX878', 'group': 'C'}, 'position': {'x': 1400, 'y':700}},
    {'data': {'id': 'X88', 'label': 'X88', 'group': 'X'}, 'position': {'x': 1500, 'y':700}},
    {'data': {'source': 'X82', 'target': 'CX878'}},
    {'data': {'source': 'X88', 'target': 'CX878'}},

    # 第九行X
    {'data': {'id': 'CX967', 'label': 'CX967', 'group': 'C'}, 'position': {'x': 1200, 'y':800}},
    {'data': {'id': 'X97', 'label': 'X97', 'group': 'X'}, 'position': {'x': 1300, 'y':800}},
    {'data': {'id': 'CX978', 'label': 'CX978', 'group': 'C'}, 'position': {'x': 1400, 'y':800}},
    {'data': {'id': 'X98', 'label': 'X98', 'group': 'X'}, 'position': {'x': 1500, 'y':800}},
    {'data': {'source': 'X97', 'target': 'CX967'}},
    {'data': {'source': 'X97', 'target': 'CX978'}},
    {'data': {'source': 'X98', 'target': 'CX978'}},

    # 第10行X
    {'data': {'id': 'CX1067', 'label': 'CX1067', 'group': 'C'}, 'position': {'x': 1200, 'y':900}},
    {'data': {'id': 'X107', 'label': 'X107', 'group': 'X'}, 'position': {'x': 1300, 'y':900}},
    {'data': {'id': 'CX1078', 'label': 'CX1078', 'group': 'C'}, 'position': {'x': 1400, 'y':900}},
    {'data': {'id': 'X108', 'label': 'X108', 'group': 'X'}, 'position': {'x': 1500, 'y':900}},
    {'data': {'source': 'X107', 'target': 'CX1067'}},
    {'data': {'source': 'X107', 'target': 'CX1078'}},
    {'data': {'source': 'X108', 'target': 'CX1078'}},

    # 第11行X
    {'data': {'id': 'CX1156', 'label': 'CX1156', 'group': 'C'}, 'position': {'x': 1000, 'y': 1000}},
    {'data': {'id': 'X117', 'label': 'X117', 'group': 'X'}, 'position': {'x': 1300, 'y':1000}},
    {'data': {'id': 'CX1178', 'label': 'CX1178', 'group': 'C'}, 'position': {'x': 1400, 'y':1000}},
    {'data': {'id': 'X118', 'label': 'X118', 'group': 'X'}, 'position': {'x': 1500, 'y':1000}},
    {'data': {'source': 'X117', 'target': 'CX1156'}},
    {'data': {'source': 'X117', 'target': 'CX1178'}},
    {'data': {'source': 'X118', 'target': 'CX1178'}},

    # 第12行X
    {'data': {'id': 'CX1267', 'label': 'CX1267', 'group': 'C'}, 'position': {'x': 1200, 'y':1100}},
    {'data': {'id': 'X127', 'label': 'X127', 'group': 'X'}, 'position': {'x': 1300, 'y':1100}},
    {'data': {'id': 'CX1278', 'label': 'CX1278', 'group': 'C'}, 'position': {'x': 1400, 'y':1100}},
    {'data': {'id': 'X128', 'label': 'X128', 'group': 'X'}, 'position': {'x': 1500, 'y':1100}},
    {'data': {'source': 'X127', 'target': 'CX1267'}},
    {'data': {'source': 'X127', 'target': 'CX1278'}},
    {'data': {'source': 'X128', 'target': 'CX1278'}},

    # 第13行X
    {'data': {'id': 'CX1356', 'label': 'CX1356', 'group': 'C'}, 'position': {'x': 1000, 'y': 1200}},
    {'data': {'id': 'X137', 'label': 'X137', 'group': 'X'}, 'position': {'x': 1300, 'y': 1200}},
    {'data': {'id': 'CX1378', 'label': 'CX1378', 'group': 'C'}, 'position': {'x': 1400, 'y': 1200}},
    {'data': {'id': 'X138', 'label': 'X138', 'group': 'X'}, 'position': {'x': 1500, 'y': 1200}},
    {'data': {'source': 'X137', 'target': 'CX1356'}},
    {'data': {'source': 'X137', 'target': 'CX1378'}},
    {'data': {'source': 'X138', 'target': 'CX1378'}},

    # 第14行X
    {'data': {'id': 'CX1445', 'label': 'CX1445', 'group': 'C'}, 'position': {'x': 800, 'y': 1300}},
    {'data': {'id': 'X147', 'label': 'X147', 'group': 'X'}, 'position': {'x': 1300, 'y': 1300}},
    {'data': {'id': 'CX1478', 'label': 'CX1478', 'group': 'C'}, 'position': {'x': 1400, 'y': 1300}},
    {'data': {'id': 'X148', 'label': 'X148', 'group': 'X'}, 'position': {'x': 1500, 'y': 1300}},
    {'data': {'source': 'X147', 'target': 'CX1445'}},
    {'data': {'source': 'X147', 'target': 'CX1478'}},
    {'data': {'source': 'X148', 'target': 'CX1478'}},

    # 第15行X
    {'data': {'id': 'CX1556', 'label': 'CX1556', 'group': 'C'}, 'position': {'x': 1000, 'y': 1400}},
    {'data': {'id': 'X156', 'label': 'X156', 'group': 'X'}, 'position': {'x': 1100, 'y': 1400}},
    {'data': {'id': 'CX1578', 'label': 'CX1578', 'group': 'C'}, 'position': {'x': 1400, 'y': 1400}},
    {'data': {'id': 'X158', 'label': 'X158', 'group': 'X'}, 'position': {'x': 1500, 'y': 1400}},
    {'data': {'source': 'X156', 'target': 'CX1556'}},
    {'data': {'source': 'X156', 'target': 'CX1578'}},
    {'data': {'source': 'X158', 'target': 'CX1578'}},

    # 第16行X
    {'data': {'id': 'X161', 'label': 'X161', 'group': 'X'}, 'position': {'x': 100, 'y': 1500}},

    # 第1行Z
    {'data': {'id': 'CZ156', 'label': 'CZ156', 'group': 'C'}, 'position': {'x': 2900, 'y': 0}},
    {'data': {'id': 'Z17', 'label': 'Z17', 'group': 'Z'}, 'position': {'x': 3200, 'y': 0}},
    {'data': {'id': 'CZ178', 'label': 'CZ178', 'group': 'C'}, 'position': {'x': 3300, 'y': 0}},
    {'data': {'id': 'Z18', 'label': 'Z18', 'group': 'Z'}, 'position': {'x': 3400, 'y': 0}},
    {'data': {'id': 'CZ189', 'label': 'CZ189', 'group': 'C'}, 'position': {'x': 3500, 'y': 0}},
    {'data': {'source': 'Z17', 'target': 'CZ156'}},
    {'data': {'source': 'Z17', 'target': 'CZ178'}},
    {'data': {'source': 'Z18', 'target': 'CZ178'}},
    {'data': {'source': 'Z18', 'target': 'CZ189'}},

    #第2行Z
    {'data': {'id': 'CZ245', 'label': 'CZ245', 'group': 'C'}, 'position': {'x': 2700, 'y': 100}},
    {'data': {'id': 'Z27', 'label': 'Z27', 'group': 'Z'}, 'position': {'x': 3200, 'y': 100}},
    {'data': {'id': 'CZ278', 'label': 'CZ278', 'group': 'C'}, 'position': {'x': 3300, 'y': 100}},
    {'data': {'id': 'Z28', 'label': 'Z28', 'group': 'Z'}, 'position': {'x': 3400, 'y': 100}},
    {'data': {'id': 'CZ289', 'label': 'CZ289', 'group': 'C'}, 'position': {'x': 3500, 'y': 100}},
    {'data': {'source': 'Z27', 'target': 'CZ245'}},
    {'data': {'source': 'Z27', 'target': 'CZ278'}},
    {'data': {'source': 'Z28', 'target': 'CZ278'}},
    {'data': {'source': 'Z28', 'target': 'CZ289'}},

    # 第3行Z
    {'data': {'id': 'Z36', 'label': 'Z36', 'group': 'Z'}, 'position': {'x': 3000, 'y': 200}},
    {'data': {'id': 'CZ378', 'label': 'CZ378', 'group': 'C'}, 'position': {'x': 3300, 'y': 200}},
    {'data': {'id': 'Z38', 'label': 'Z38', 'group': 'Z'}, 'position': {'x': 3400, 'y': 200}},
    {'data': {'id': 'CZ389', 'label': 'CZ389', 'group': 'C'}, 'position': {'x': 3500, 'y': 200}},
    {'data': {'source': 'Z36', 'target': 'CZ378'}},
    {'data': {'source': 'Z38', 'target': 'CZ378'}},
    {'data': {'source': 'Z38', 'target': 'CZ389'}},

    # 第4行Z
    {'data': {'id': 'CZ434', 'label': 'CZ434', 'group': 'C'}, 'position': {'x': 2500, 'y': 300}},
    {'data': {'id': 'Z47', 'label': 'Z47', 'group': 'Z'}, 'position': {'x': 3200, 'y': 300}},
    {'data': {'id': 'CZ478', 'label': 'CZ478', 'group': 'C'}, 'position': {'x': 3300, 'y': 300}},
    {'data': {'id': 'Z48', 'label': 'Z48', 'group': 'Z'}, 'position': {'x': 3400, 'y': 300}},
    {'data': {'id': 'CZ489', 'label': 'CZ489', 'group': 'C'}, 'position': {'x': 3500, 'y': 300}},
    {'data': {'source': 'Z47', 'target': 'CZ434'}},
    {'data': {'source': 'Z47', 'target': 'CZ478'}},
    {'data': {'source': 'Z48', 'target': 'CZ478'}},
    {'data': {'source': 'Z48', 'target': 'CZ489'}},

    # 第5行Z
    {'data': {'id': 'Z56', 'label': 'Z56', 'group': 'Z'}, 'position': {'x': 3000, 'y': 400}},
    {'data': {'id': 'CZ578', 'label': 'CZ578', 'group': 'C'}, 'position': {'x': 3300, 'y': 400}},
    {'data': {'id': 'Z58', 'label': 'Z58', 'group': 'Z'}, 'position': {'x': 3400, 'y': 400}},
    {'data': {'id': 'CZ589', 'label': 'CZ589', 'group': 'C'}, 'position': {'x': 3500, 'y': 400}},
    {'data': {'source': 'Z56', 'target': 'CZ578'}},
    {'data': {'source': 'Z58', 'target': 'CZ578'}},
    {'data': {'source': 'Z58', 'target': 'CZ589'}},

    # 第6行Z
    {'data': {'id': 'Z66', 'label': 'Z66', 'group': 'Z'}, 'position': {'x': 3000, 'y': 500}},
    {'data': {'id': 'CZ678', 'label': 'CZ678', 'group': 'C'}, 'position': {'x': 3300, 'y': 500}},
    {'data': {'id': 'Z68', 'label': 'Z68', 'group': 'Z'}, 'position': {'x': 3400, 'y': 500}},
    {'data': {'id': 'CZ689', 'label': 'CZ689', 'group': 'C'}, 'position': {'x': 3500, 'y': 500}},
    {'data': {'source': 'Z66', 'target': 'CZ678'}},
    {'data': {'source': 'Z68', 'target': 'CZ678'}},
    {'data': {'source': 'Z68', 'target': 'CZ689'}},

    # 第7行Z
    {'data': {'id': 'Z75', 'label': 'Z75', 'group': 'Z'}, 'position': {'x': 2800, 'y': 600}},
    {'data': {'id': 'CZ778', 'label': 'CZ778', 'group': 'C'}, 'position': {'x': 3300, 'y': 600}},
    {'data': {'id': 'Z78', 'label': 'Z78', 'group': 'Z'}, 'position': {'x': 3400, 'y': 600}},
    {'data': {'id': 'CZ789', 'label': 'CZ789', 'group': 'C'}, 'position': {'x': 3500, 'y': 600}},
    {'data': {'source': 'Z75', 'target': 'CZ778'}},
    {'data': {'source': 'Z78', 'target': 'CZ778'}},
    {'data': {'source': 'Z78', 'target': 'CZ789'}},

    # 第8行Z
    {'data': {'id': 'CZ823', 'label': 'CZ823', 'group': 'C'}, 'position': {'x': 2300, 'y': 700}},
    {'data': {'id': 'Z87', 'label': 'Z87', 'group': 'Z'}, 'position': {'x': 3200, 'y': 700}},
    {'data': {'id': 'CZ878', 'label': 'CZ878', 'group': 'C'}, 'position': {'x': 3300, 'y': 700}},
    {'data': {'id': 'Z88', 'label': 'Z88', 'group': 'Z'}, 'position': {'x': 3400, 'y': 700}},
    {'data': {'id': 'CZ889', 'label': 'CZ889', 'group': 'C'}, 'position': {'x': 3500, 'y': 700}},
    {'data': {'source': 'Z87', 'target': 'CZ823'}},
    {'data': {'source': 'Z87', 'target': 'CZ878'}},
    {'data': {'source': 'Z88', 'target': 'CZ878'}},
    {'data': {'source': 'Z88', 'target': 'CZ889'}},

    # 第9行Z
    {'data': {'id': 'Z96', 'label': 'Z96', 'group': 'Z'}, 'position': {'x': 3000, 'y': 800}},
    {'data': {'id': 'CZ978', 'label': 'CZ978', 'group': 'C'}, 'position': {'x': 3300, 'y': 800}},
    {'data': {'id': 'Z98', 'label': 'Z98', 'group': 'Z'}, 'position': {'x': 3400, 'y': 800}},
    {'data': {'id': 'CZ989', 'label': 'CZ989', 'group': 'C'}, 'position': {'x': 3500, 'y': 800}},
    {'data': {'source': 'Z96', 'target': 'CZ978'}},
    {'data': {'source': 'Z98', 'target': 'CZ978'}},
    {'data': {'source': 'Z98', 'target': 'CZ989'}},

    # 第10行Z
    {'data': {'id': 'Z106', 'label': 'Z106', 'group': 'Z'}, 'position': {'x': 3000, 'y': 900}},
    {'data': {'id': 'CZ1078', 'label': 'CZ1078', 'group': 'C'}, 'position': {'x': 3300, 'y': 900}},
    {'data': {'id': 'Z108', 'label': 'Z108', 'group': 'Z'}, 'position': {'x': 3400, 'y': 900}},
    {'data': {'id': 'CZ1089', 'label': 'CZ1089', 'group': 'C'}, 'position': {'x': 3500, 'y': 900}},
    {'data': {'source': 'Z106', 'target': 'CZ1078'}},
    {'data': {'source': 'Z108', 'target': 'CZ1078'}},
    {'data': {'source': 'Z108', 'target': 'CZ1089'}},

    # 第11行Z
    {'data': {'id': 'Z115', 'label': 'Z115', 'group': 'Z'}, 'position': {'x': 2800, 'y': 1000}},
    {'data': {'id': 'CZ1178', 'label': 'CZ1178', 'group': 'C'}, 'position': {'x': 3300, 'y': 1000}},
    {'data': {'id': 'Z118', 'label': 'Z118', 'group': 'Z'}, 'position': {'x': 3400, 'y': 1000}},
    {'data': {'id': 'CZ1189', 'label': 'CZ1189', 'group': 'C'}, 'position': {'x': 3500, 'y': 1000}},
    {'data': {'source': 'Z115', 'target': 'CZ1178'}},
    {'data': {'source': 'Z118', 'target': 'CZ1178'}},
    {'data': {'source': 'Z118', 'target': 'CZ1189'}},

    # 第12行Z
    {'data': {'id': 'Z126', 'label': 'Z126', 'group': 'Z'}, 'position': {'x': 3000, 'y': 1100}},
    {'data': {'id': 'CZ1278', 'label': 'CZ1278', 'group': 'C'}, 'position': {'x': 3300, 'y': 1100}},
    {'data': {'id': 'Z128', 'label': 'Z128', 'group': 'Z'}, 'position': {'x': 3400, 'y': 1100}},
    {'data': {'id': 'CZ1289', 'label': 'CZ1289', 'group': 'C'}, 'position': {'x': 3500, 'y': 1100}},
    {'data': {'source': 'Z126', 'target': 'CZ1278'}},
    {'data': {'source': 'Z128', 'target': 'CZ1278'}},
    {'data': {'source': 'Z128', 'target': 'CZ1289'}},

    # 第13行Z
    {'data': {'id': 'Z135', 'label': 'Z135', 'group': 'Z'}, 'position': {'x': 2800, 'y': 1200}},
    {'data': {'id': 'CZ1378', 'label': 'CZ1378', 'group': 'C'}, 'position': {'x': 3300, 'y': 1200}},
    {'data': {'id': 'Z138', 'label': 'Z138', 'group': 'Z'}, 'position': {'x': 3400, 'y': 1200}},
    {'data': {'id': 'CZ1389', 'label': 'CZ1389', 'group': 'C'}, 'position': {'x': 3500, 'y': 1200}},
    {'data': {'source': 'Z135', 'target': 'CZ1378'}},
    {'data': {'source': 'Z138', 'target': 'CZ1378'}},
    {'data': {'source': 'Z138', 'target': 'CZ1389'}},

    # 第14行Z
    {'data': {'id': 'Z144', 'label': 'Z144', 'group': 'Z'}, 'position': {'x': 2600, 'y': 1300}},
    {'data': {'id': 'CZ1478', 'label': 'CZ1478', 'group': 'C'}, 'position': {'x': 3300, 'y': 1300}},
    {'data': {'id': 'Z148', 'label': 'Z148', 'group': 'Z'}, 'position': {'x': 3400, 'y': 1300}},
    {'data': {'id': 'CZ1489', 'label': 'CZ1489', 'group': 'C'}, 'position': {'x': 3500, 'y': 1300}},
    {'data': {'source': 'Z144', 'target': 'CZ1478'}},
    {'data': {'source': 'Z148', 'target': 'CZ1478'}},
    {'data': {'source': 'Z148', 'target': 'CZ1489'}},

    # 第15行Z
    {'data': {'id': 'Z155', 'label': 'Z155', 'group': 'Z'}, 'position': {'x': 2800, 'y': 1400}},
    {'data': {'id': 'CZ1567', 'label': 'CZ1567', 'group': 'C'}, 'position': {'x': 3100, 'y': 1400}},
    {'data': {'id': 'Z157', 'label': 'Z157', 'group': 'Z'}, 'position': {'x': 3200, 'y': 1400}},
    {'data': {'id': 'CZ1578', 'label': 'CZ1578', 'group': 'C'}, 'position': {'x': 3300, 'y': 1400}},
    {'data': {'id': 'Z158', 'label': 'Z158', 'group': 'Z'}, 'position': {'x': 3400, 'y': 1400}},
    {'data': {'id': 'CZ1589', 'label': 'CZ1589', 'group': 'C'}, 'position': {'x': 3500, 'y': 1400}},
    {'data': {'source': 'Z155', 'target': 'CZ1567'}},
    {'data': {'source': 'Z157', 'target': 'CZ1567'}},
    {'data': {'source': 'Z157', 'target': 'CZ1578'}},
    {'data': {'source': 'Z158', 'target': 'CZ1578'}},
    {'data': {'source': 'Z158', 'target': 'CZ1589'}},

    # 第16行Z
    {'data': {'id': 'CZ1612', 'label': 'CZ1612', 'group': 'C'}, 'position': {'x': 2100, 'y': 1500}},

]
CNOT1_edges =[{'data': {'source': 'X161', 'target': 'CX1556'}},
              {'data': {'source': 'Z155', 'target': 'CZ1612'}},]

CNOT2X = ['CX967', 'CX1067', 'CX1156', 'CX1267', 'CX1356', 'CX1445', 'CX1556']  # 按需扩展
CNOT2X_edges = [{'data': {'source': 'X82','target': target,}} for target in CNOT2X]
CNOT2Z = ['Z96', 'Z106', 'Z115', 'Z126', 'Z135', 'Z144', 'Z155']
CNOT2Z_edges = [{'data': {'source': 'CZ823','target': target,}} for target in CNOT2Z]

CNOT3X = ['CX567', 'CX667', 'CX756', 'CX1267', 'CX1356', 'CX1445', 'CX1556']  # 按需扩展
CNOT3X_edges = [{'data': {'source': 'X43','target': target,}} for target in CNOT3X]
CNOT3Z = ['Z56', 'Z66', 'Z75', 'Z126', 'Z135', 'Z144', 'Z155']
CNOT3Z_edges = [{'data': {'source': 'CZ434','target': target,}} for target in CNOT3Z]

CNOT4X = ['CX367', 'CX667', 'CX756', 'CX1067', 'CX1156', 'CX1445', 'CX1556']  # 按需扩展
CNOT4X_edges = [{'data': {'source': 'X24','target': target,}} for target in CNOT4X]
CNOT4Z = ['Z36', 'Z66', 'Z75', 'Z106', 'Z115', 'Z144', 'Z155']
CNOT4Z_edges = [{'data': {'source': 'CZ245','target': target,}} for target in CNOT4Z]

CNOT5X = ['CX367', 'CX567', 'CX756', 'CX967', 'CX1156', 'CX1356', 'CX1556']  # 按需扩展
CNOT5X_edges = [{'data': {'source': 'X15','target': target,}} for target in CNOT5X]
CNOT5Z = ['Z36', 'Z56', 'Z75', 'Z96', 'Z115', 'Z135', 'Z155']
CNOT5Z_edges = [{'data': {'source': 'CZ156','target': target,}} for target in CNOT5Z]

CNOT6X = ['CX367', 'CX567', 'CX667', 'CX967', 'CX1067', 'CX1267']  # 按需扩展
CNOT6X_edges = [{'data': {'source': 'X156','target': target,}} for target in CNOT6X]
CNOT6Z = ['Z36', 'Z56', 'Z66', 'Z96', 'Z106', 'Z126']
CNOT6Z_edges = [{'data': {'source': 'CZ1567','target': target,}} for target in CNOT6Z]
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
    TGDeiso.run(host='0.0.0.0', port=8052, debug=True)  # 必须设置host参数
