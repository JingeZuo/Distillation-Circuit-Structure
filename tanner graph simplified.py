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
    {'data': {'id': 'CZ178', 'label': 'CZ178', 'group': 'C'}, 'position': {'x': 3100, 'y': 0}},
    {'data': {'id': 'Z18', 'label': 'Z18', 'group': 'Z'}, 'position': {'x': 3200, 'y': 0}},
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
    {'data': {'source': 'Z17', 'target': 'CZ178'}},
    {'data': {'source': 'Z18', 'target': 'CZ178'}},
    {'data': {'source': 'Z12', 'target': 'CZ112'}},

    #第2行Z
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
    {'data': {'id': 'CZ278', 'label': 'CZ278', 'group': 'C'}, 'position': {'x': 3100, 'y': 100}},
    {'data': {'id': 'Z28', 'label': 'Z28', 'group': 'Z'}, 'position': {'x': 3200, 'y': 100}},
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
    {'data': {'source': 'Z27', 'target': 'CZ278'}},
    {'data': {'source': 'Z28', 'target': 'CZ278'}},
    {'data': {'source': 'Z22', 'target': 'CZ212'}},

    # 第3行Z
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
    {'data': {'id': 'CZ378', 'label': 'CZ378', 'group': 'C'}, 'position': {'x': 3100, 'y': 200}},
    {'data': {'id': 'Z38', 'label': 'Z38', 'group': 'Z'}, 'position': {'x': 3200, 'y': 200}},
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
    {'data': {'source': 'Z37', 'target': 'CZ378'}},
    {'data': {'source': 'Z38', 'target': 'CZ378'}},

    # 第4行Z
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
    {'data': {'id': 'CZ478', 'label': 'CZ478', 'group': 'C'}, 'position': {'x': 3100, 'y': 300}},
    {'data': {'id': 'Z48', 'label': 'Z48', 'group': 'Z'}, 'position': {'x': 3200, 'y': 300}},
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
    {'data': {'source': 'Z47', 'target': 'CZ478'}},
    {'data': {'source': 'Z48', 'target': 'CZ478'}},
    {'data': {'source': 'Z42', 'target': 'CZ412'}},

    # 第5行Z
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
    {'data': {'id': 'CZ578', 'label': 'CZ578', 'group': 'C'}, 'position': {'x': 3100, 'y': 400}},
    {'data': {'id': 'Z58', 'label': 'Z58', 'group': 'Z'}, 'position': {'x': 3200, 'y': 400}},
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
    {'data': {'source': 'Z57', 'target': 'CZ578'}},
    {'data': {'source': 'Z58', 'target': 'CZ578'}},

    # 第6行Z
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
    {'data': {'id': 'CZ678', 'label': 'CZ678', 'group': 'C'}, 'position': {'x': 3100, 'y': 500}},
    {'data': {'id': 'Z68', 'label': 'Z68', 'group': 'Z'}, 'position': {'x': 3200, 'y': 500}},
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
    {'data': {'source': 'Z67', 'target': 'CZ678'}},
    {'data': {'source': 'Z68', 'target': 'CZ678'}},

    # 第7行Z
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
    {'data': {'id': 'CZ778', 'label': 'CZ778', 'group': 'C'}, 'position': {'x': 3100, 'y': 600}},
    {'data': {'id': 'Z78', 'label': 'Z78', 'group': 'Z'}, 'position': {'x': 3200, 'y': 600}},
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
    {'data': {'source': 'Z77', 'target': 'CZ778'}},
    {'data': {'source': 'Z78', 'target': 'CZ778'}},

    # 第8行Z
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
    {'data': {'id': 'CZ878', 'label': 'CZ878', 'group': 'C'}, 'position': {'x': 3100, 'y': 700}},
    {'data': {'id': 'Z88', 'label': 'Z88', 'group': 'Z'}, 'position': {'x': 3200, 'y': 700}},
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
    {'data': {'source': 'Z87', 'target': 'CZ878'}},
    {'data': {'source': 'Z88', 'target': 'CZ878'}},
    {'data': {'source': 'Z82', 'target': 'CZ812'}},

    # 第9行Z
    {'data': {'id': 'Z92', 'label': 'Z92', 'group': 'Z'}, 'position': {'x': 2000, 'y': 800}},
    {'data': {'id': 'CZ923', 'label': 'CZ923', 'group': 'C'}, 'position': {'x': 2100, 'y': 800}},
    {'data': {'id': 'Z93', 'label': 'Z93', 'group': 'Z'}, 'position': {'x': 2200, 'y': 800}},
    {'data': {'id': 'CZ934', 'label': 'CZ934', 'group': 'C'}, 'position': {'x': 2300, 'y': 800}},
    {'data': {'id': 'Z94', 'label': 'Z94', 'group': 'Z'}, 'position': {'x': 2400, 'y': 800}},
    {'data': {'id': 'CZ945', 'label': 'CZ945', 'group': 'C'}, 'position': {'x': 2500, 'y': 800}},
    {'data': {'id': 'Z95', 'label': 'Z95', 'group': 'Z'}, 'position': {'x': 2600, 'y': 800}},
    {'data': {'id': 'CZ956', 'label': 'CZ956', 'group': 'C'}, 'position': {'x': 2700, 'y': 800}},
    {'data': {'id': 'Z96', 'label': 'Z96', 'group': 'Z'}, 'position': {'x': 2800, 'y': 800}},
    {'data': {'id': 'CZ967', 'label': 'CZ967', 'group': 'C'}, 'position': {'x': 2900, 'y': 800}},
    {'data': {'id': 'Z97', 'label': 'Z97', 'group': 'Z'}, 'position': {'x': 3000, 'y': 800}},
    {'data': {'id': 'CZ978', 'label': 'CZ978', 'group': 'C'}, 'position': {'x': 3100, 'y': 800}},
    {'data': {'id': 'Z98', 'label': 'Z98', 'group': 'Z'}, 'position': {'x': 3200, 'y': 800}},
    {'data': {'source': 'Z92', 'target': 'CZ923'}},
    {'data': {'source': 'Z93', 'target': 'CZ923'}},
    {'data': {'source': 'Z93', 'target': 'CZ934'}},
    {'data': {'source': 'Z94', 'target': 'CZ934'}},
    {'data': {'source': 'Z94', 'target': 'CZ945'}},
    {'data': {'source': 'Z95', 'target': 'CZ945'}},
    {'data': {'source': 'Z95', 'target': 'CZ956'}},
    {'data': {'source': 'Z96', 'target': 'CZ956'}},
    {'data': {'source': 'Z96', 'target': 'CZ967'}},
    {'data': {'source': 'Z97', 'target': 'CZ967'}},
    {'data': {'source': 'Z97', 'target': 'CZ978'}},
    {'data': {'source': 'Z98', 'target': 'CZ978'}},

    # 第10行Z
    {'data': {'id': 'Z102', 'label': 'Z102', 'group': 'Z'}, 'position': {'x': 2000, 'y': 900}},
    {'data': {'id': 'CZ1023', 'label': 'CZ1023', 'group': 'C'}, 'position': {'x': 2100, 'y': 900}},
    {'data': {'id': 'Z103', 'label': 'Z103', 'group': 'Z'}, 'position': {'x': 2200, 'y': 900}},
    {'data': {'id': 'CZ1034', 'label': 'CZ1034', 'group': 'C'}, 'position': {'x': 2300, 'y': 900}},
    {'data': {'id': 'Z104', 'label': 'Z104', 'group': 'Z'}, 'position': {'x': 2400, 'y': 900}},
    {'data': {'id': 'CZ1045', 'label': 'CZ1045', 'group': 'C'}, 'position': {'x': 2500, 'y': 900}},
    {'data': {'id': 'Z105', 'label': 'Z105', 'group': 'Z'}, 'position': {'x': 2600, 'y': 900}},
    {'data': {'id': 'CZ1056', 'label': 'CZ1056', 'group': 'C'}, 'position': {'x': 2700, 'y': 900}},
    {'data': {'id': 'Z106', 'label': 'Z106', 'group': 'Z'}, 'position': {'x': 2800, 'y': 900}},
    {'data': {'id': 'CZ1067', 'label': 'CZ1067', 'group': 'C'}, 'position': {'x': 2900, 'y': 900}},
    {'data': {'id': 'Z107', 'label': 'Z107', 'group': 'Z'}, 'position': {'x': 3000, 'y': 900}},
    {'data': {'id': 'CZ1078', 'label': 'CZ1078', 'group': 'C'}, 'position': {'x': 3100, 'y': 900}},
    {'data': {'id': 'Z108', 'label': 'Z108', 'group': 'Z'}, 'position': {'x': 3200, 'y': 900}},
    {'data': {'source': 'Z102', 'target': 'CZ1023'}},
    {'data': {'source': 'Z103', 'target': 'CZ1023'}},
    {'data': {'source': 'Z103', 'target': 'CZ1034'}},
    {'data': {'source': 'Z104', 'target': 'CZ1034'}},
    {'data': {'source': 'Z104', 'target': 'CZ1045'}},
    {'data': {'source': 'Z105', 'target': 'CZ1045'}},
    {'data': {'source': 'Z105', 'target': 'CZ1056'}},
    {'data': {'source': 'Z106', 'target': 'CZ1056'}},
    {'data': {'source': 'Z106', 'target': 'CZ1067'}},
    {'data': {'source': 'Z107', 'target': 'CZ1067'}},
    {'data': {'source': 'Z107', 'target': 'CZ1078'}},
    {'data': {'source': 'Z108', 'target': 'CZ1078'}},

    # 第11行Z
    {'data': {'id': 'Z112', 'label': 'Z112', 'group': 'Z'}, 'position': {'x': 2000, 'y': 1000}},
    {'data': {'id': 'CZ1123', 'label': 'CZ1123', 'group': 'C'}, 'position': {'x': 2100, 'y': 1000}},
    {'data': {'id': 'Z113', 'label': 'Z113', 'group': 'Z'}, 'position': {'x': 2200, 'y': 1000}},
    {'data': {'id': 'CZ1134', 'label': 'CZ1134', 'group': 'C'}, 'position': {'x': 2300, 'y': 1000}},
    {'data': {'id': 'Z114', 'label': 'Z114', 'group': 'Z'}, 'position': {'x': 2400, 'y': 1000}},
    {'data': {'id': 'CZ1145', 'label': 'CZ1145', 'group': 'C'}, 'position': {'x': 2500, 'y': 1000}},
    {'data': {'id': 'Z115', 'label': 'Z115', 'group': 'Z'}, 'position': {'x': 2600, 'y': 1000}},
    {'data': {'id': 'CZ1156', 'label': 'CZ1156', 'group': 'C'}, 'position': {'x': 2700, 'y': 1000}},
    {'data': {'id': 'Z116', 'label': 'Z116', 'group': 'Z'}, 'position': {'x': 2800, 'y': 1000}},
    {'data': {'id': 'CZ1167', 'label': 'CZ1167', 'group': 'C'}, 'position': {'x': 2900, 'y': 1000}},
    {'data': {'id': 'Z117', 'label': 'Z117', 'group': 'Z'}, 'position': {'x': 3000, 'y': 1000}},
    {'data': {'id': 'CZ1178', 'label': 'CZ1178', 'group': 'C'}, 'position': {'x': 3100, 'y': 1000}},
    {'data': {'id': 'Z118', 'label': 'Z118', 'group': 'Z'}, 'position': {'x': 3200, 'y': 1000}},
    {'data': {'source': 'Z112', 'target': 'CZ1123'}},
    {'data': {'source': 'Z113', 'target': 'CZ1123'}},
    {'data': {'source': 'Z113', 'target': 'CZ1134'}},
    {'data': {'source': 'Z114', 'target': 'CZ1134'}},
    {'data': {'source': 'Z114', 'target': 'CZ1145'}},
    {'data': {'source': 'Z115', 'target': 'CZ1145'}},
    {'data': {'source': 'Z115', 'target': 'CZ1156'}},
    {'data': {'source': 'Z116', 'target': 'CZ1156'}},
    {'data': {'source': 'Z116', 'target': 'CZ1167'}},
    {'data': {'source': 'Z117', 'target': 'CZ1167'}},
    {'data': {'source': 'Z117', 'target': 'CZ1178'}},
    {'data': {'source': 'Z118', 'target': 'CZ1178'}},

    # 第12行Z
    {'data': {'id': 'Z122', 'label': 'Z122', 'group': 'Z'}, 'position': {'x': 2000, 'y': 1100}},
    {'data': {'id': 'CZ1223', 'label': 'CZ1223', 'group': 'C'}, 'position': {'x': 2100, 'y': 1100}},
    {'data': {'id': 'Z123', 'label': 'Z123', 'group': 'Z'}, 'position': {'x': 2200, 'y': 1100}},
    {'data': {'id': 'CZ1234', 'label': 'CZ1234', 'group': 'C'}, 'position': {'x': 2300, 'y': 1100}},
    {'data': {'id': 'Z124', 'label': 'Z124', 'group': 'Z'}, 'position': {'x': 2400, 'y': 1100}},
    {'data': {'id': 'CZ1245', 'label': 'CZ1245', 'group': 'C'}, 'position': {'x': 2500, 'y': 1100}},
    {'data': {'id': 'Z125', 'label': 'Z125', 'group': 'Z'}, 'position': {'x': 2600, 'y': 1100}},
    {'data': {'id': 'CZ1256', 'label': 'CZ1256', 'group': 'C'}, 'position': {'x': 2700, 'y': 1100}},
    {'data': {'id': 'Z126', 'label': 'Z126', 'group': 'Z'}, 'position': {'x': 2800, 'y': 1100}},
    {'data': {'id': 'CZ1267', 'label': 'CZ1267', 'group': 'C'}, 'position': {'x': 2900, 'y': 1100}},
    {'data': {'id': 'Z127', 'label': 'Z127', 'group': 'Z'}, 'position': {'x': 3000, 'y': 1100}},
    {'data': {'id': 'CZ1278', 'label': 'CZ1278', 'group': 'C'}, 'position': {'x': 3100, 'y': 1100}},
    {'data': {'id': 'Z128', 'label': 'Z128', 'group': 'Z'}, 'position': {'x': 3200, 'y': 1100}},
    {'data': {'source': 'Z122', 'target': 'CZ1223'}},
    {'data': {'source': 'Z123', 'target': 'CZ1223'}},
    {'data': {'source': 'Z123', 'target': 'CZ1234'}},
    {'data': {'source': 'Z124', 'target': 'CZ1234'}},
    {'data': {'source': 'Z124', 'target': 'CZ1245'}},
    {'data': {'source': 'Z125', 'target': 'CZ1245'}},
    {'data': {'source': 'Z125', 'target': 'CZ1256'}},
    {'data': {'source': 'Z126', 'target': 'CZ1256'}},
    {'data': {'source': 'Z126', 'target': 'CZ1267'}},
    {'data': {'source': 'Z127', 'target': 'CZ1267'}},
    {'data': {'source': 'Z127', 'target': 'CZ1278'}},
    {'data': {'source': 'Z128', 'target': 'CZ1278'}},

    # 第13行Z
    {'data': {'id': 'Z132', 'label': 'Z132', 'group': 'Z'}, 'position': {'x': 2000, 'y': 1200}},
    {'data': {'id': 'CZ1323', 'label': 'CZ1323', 'group': 'C'}, 'position': {'x': 2100, 'y': 1200}},
    {'data': {'id': 'Z133', 'label': 'Z133', 'group': 'Z'}, 'position': {'x': 2200, 'y': 1200}},
    {'data': {'id': 'CZ1334', 'label': 'CZ1334', 'group': 'C'}, 'position': {'x': 2300, 'y': 1200}},
    {'data': {'id': 'Z134', 'label': 'Z134', 'group': 'Z'}, 'position': {'x': 2400, 'y': 1200}},
    {'data': {'id': 'CZ1345', 'label': 'CZ1345', 'group': 'C'}, 'position': {'x': 2500, 'y': 1200}},
    {'data': {'id': 'Z135', 'label': 'Z135', 'group': 'Z'}, 'position': {'x': 2600, 'y': 1200}},
    {'data': {'id': 'CZ1356', 'label': 'CZ1356', 'group': 'C'}, 'position': {'x': 2700, 'y': 1200}},
    {'data': {'id': 'Z136', 'label': 'Z136', 'group': 'Z'}, 'position': {'x': 2800, 'y': 1200}},
    {'data': {'id': 'CZ1367', 'label': 'CZ1367', 'group': 'C'}, 'position': {'x': 2900, 'y': 1200}},
    {'data': {'id': 'Z137', 'label': 'Z137', 'group': 'Z'}, 'position': {'x': 3000, 'y': 1200}},
    {'data': {'id': 'CZ1378', 'label': 'CZ1378', 'group': 'C'}, 'position': {'x': 3100, 'y': 1200}},
    {'data': {'id': 'Z138', 'label': 'Z138', 'group': 'Z'}, 'position': {'x': 3200, 'y': 1200}},
    {'data': {'source': 'Z132', 'target': 'CZ1323'}},
    {'data': {'source': 'Z133', 'target': 'CZ1323'}},
    {'data': {'source': 'Z133', 'target': 'CZ1334'}},
    {'data': {'source': 'Z134', 'target': 'CZ1334'}},
    {'data': {'source': 'Z134', 'target': 'CZ1345'}},
    {'data': {'source': 'Z135', 'target': 'CZ1345'}},
    {'data': {'source': 'Z135', 'target': 'CZ1356'}},
    {'data': {'source': 'Z136', 'target': 'CZ1356'}},
    {'data': {'source': 'Z136', 'target': 'CZ1367'}},
    {'data': {'source': 'Z137', 'target': 'CZ1367'}},
    {'data': {'source': 'Z137', 'target': 'CZ1378'}},
    {'data': {'source': 'Z138', 'target': 'CZ1378'}},

    # 第14行Z
    {'data': {'id': 'Z142', 'label': 'Z142', 'group': 'Z'}, 'position': {'x': 2000, 'y': 1300}},
    {'data': {'id': 'CZ1423', 'label': 'CZ1423', 'group': 'C'}, 'position': {'x': 2100, 'y': 1300}},
    {'data': {'id': 'Z143', 'label': 'Z143', 'group': 'Z'}, 'position': {'x': 2200, 'y': 1300}},
    {'data': {'id': 'CZ1434', 'label': 'CZ1434', 'group': 'C'}, 'position': {'x': 2300, 'y': 1300}},
    {'data': {'id': 'Z144', 'label': 'Z144', 'group': 'Z'}, 'position': {'x': 2400, 'y': 1300}},
    {'data': {'id': 'CZ1445', 'label': 'CZ1445', 'group': 'C'}, 'position': {'x': 2500, 'y': 1300}},
    {'data': {'id': 'Z145', 'label': 'Z145', 'group': 'Z'}, 'position': {'x': 2600, 'y': 1300}},
    {'data': {'id': 'CZ1456', 'label': 'CZ1456', 'group': 'C'}, 'position': {'x': 2700, 'y': 1300}},
    {'data': {'id': 'Z146', 'label': 'Z146', 'group': 'Z'}, 'position': {'x': 2800, 'y': 1300}},
    {'data': {'id': 'CZ1467', 'label': 'CZ1467', 'group': 'C'}, 'position': {'x': 2900, 'y': 1300}},
    {'data': {'id': 'Z147', 'label': 'Z147', 'group': 'Z'}, 'position': {'x': 3000, 'y': 1300}},
    {'data': {'id': 'CZ1478', 'label': 'CZ1478', 'group': 'C'}, 'position': {'x': 3100, 'y': 1300}},
    {'data': {'id': 'Z148', 'label': 'Z148', 'group': 'Z'}, 'position': {'x': 3200, 'y': 1300}},
    {'data': {'source': 'Z142', 'target': 'CZ1423'}},
    {'data': {'source': 'Z143', 'target': 'CZ1423'}},
    {'data': {'source': 'Z143', 'target': 'CZ1434'}},
    {'data': {'source': 'Z144', 'target': 'CZ1434'}},
    {'data': {'source': 'Z144', 'target': 'CZ1445'}},
    {'data': {'source': 'Z145', 'target': 'CZ1445'}},
    {'data': {'source': 'Z145', 'target': 'CZ1456'}},
    {'data': {'source': 'Z146', 'target': 'CZ1456'}},
    {'data': {'source': 'Z146', 'target': 'CZ1467'}},
    {'data': {'source': 'Z147', 'target': 'CZ1467'}},
    {'data': {'source': 'Z147', 'target': 'CZ1478'}},
    {'data': {'source': 'Z148', 'target': 'CZ1478'}},

    # 第15行Z
    {'data': {'id': 'Z152', 'label': 'Z152', 'group': 'Z'}, 'position': {'x': 2000, 'y': 1400}},
    {'data': {'id': 'CZ1523', 'label': 'CZ1523', 'group': 'C'}, 'position': {'x': 2100, 'y': 1400}},
    {'data': {'id': 'Z153', 'label': 'Z153', 'group': 'Z'}, 'position': {'x': 2200, 'y': 1400}},
    {'data': {'id': 'CZ1534', 'label': 'CZ1534', 'group': 'C'}, 'position': {'x': 2300, 'y': 1400}},
    {'data': {'id': 'Z154', 'label': 'Z154', 'group': 'Z'}, 'position': {'x': 2400, 'y': 1400}},
    {'data': {'id': 'CZ1545', 'label': 'CZ1545', 'group': 'C'}, 'position': {'x': 2500, 'y': 1400}},
    {'data': {'id': 'Z155', 'label': 'Z155', 'group': 'Z'}, 'position': {'x': 2600, 'y': 1400}},
    {'data': {'id': 'CZ1556', 'label': 'CZ1556', 'group': 'C'}, 'position': {'x': 2700, 'y': 1400}},
    {'data': {'id': 'Z156', 'label': 'Z156', 'group': 'Z'}, 'position': {'x': 2800, 'y': 1400}},
    {'data': {'id': 'CZ1567', 'label': 'CZ1567', 'group': 'C'}, 'position': {'x': 2900, 'y': 1400}},
    {'data': {'id': 'Z157', 'label': 'Z157', 'group': 'Z'}, 'position': {'x': 3000, 'y': 1400}},
    {'data': {'id': 'CZ1578', 'label': 'CZ1578', 'group': 'C'}, 'position': {'x': 3100, 'y': 1400}},
    {'data': {'id': 'Z158', 'label': 'Z158', 'group': 'Z'}, 'position': {'x': 3200, 'y': 1400}},
    {'data': {'source': 'Z152', 'target': 'CZ1523'}},
    {'data': {'source': 'Z153', 'target': 'CZ1523'}},
    {'data': {'source': 'Z153', 'target': 'CZ1534'}},
    {'data': {'source': 'Z154', 'target': 'CZ1534'}},
    {'data': {'source': 'Z154', 'target': 'CZ1545'}},
    {'data': {'source': 'Z155', 'target': 'CZ1545'}},
    {'data': {'source': 'Z155', 'target': 'CZ1556'}},
    {'data': {'source': 'Z156', 'target': 'CZ1556'}},
    {'data': {'source': 'Z156', 'target': 'CZ1567'}},
    {'data': {'source': 'Z157', 'target': 'CZ1567'}},
    {'data': {'source': 'Z157', 'target': 'CZ1578'}},
    {'data': {'source': 'Z158', 'target': 'CZ1578'}},

    # 第16行Z
    {'data': {'id': 'CZ1612', 'label': 'CZ1612', 'group': 'C'}, 'position': {'x': 1900, 'y': 1500}},
    {'data': {'id': 'Z162', 'label': 'Z162', 'group': 'Z'}, 'position': {'x': 2000, 'y': 1500}},
    {'data': {'id': 'CZ1623', 'label': 'CZ1623', 'group': 'C'}, 'position': {'x': 2100, 'y': 1500}},
    {'data': {'id': 'Z163', 'label': 'Z163', 'group': 'Z'}, 'position': {'x': 2200, 'y': 1500}},
    {'data': {'id': 'CZ1634', 'label': 'CZ1634', 'group': 'C'}, 'position': {'x': 2300, 'y': 1500}},
    {'data': {'id': 'Z164', 'label': 'Z164', 'group': 'Z'}, 'position': {'x': 2400, 'y': 1500}},
    {'data': {'id': 'CZ1645', 'label': 'CZ1645', 'group': 'C'}, 'position': {'x': 2500, 'y': 1500}},
    {'data': {'id': 'Z165', 'label': 'Z165', 'group': 'Z'}, 'position': {'x': 2600, 'y': 1500}},
    {'data': {'id': 'CZ1656', 'label': 'CZ1656', 'group': 'C'}, 'position': {'x': 2700, 'y': 1500}},
    {'data': {'id': 'Z166', 'label': 'Z166', 'group': 'Z'}, 'position': {'x': 2800, 'y': 1500}},
    {'data': {'id': 'CZ1667', 'label': 'CZ1667', 'group': 'C'}, 'position': {'x': 2900, 'y': 1500}},
    {'data': {'id': 'Z167', 'label': 'Z167', 'group': 'Z'}, 'position': {'x': 3000, 'y': 1500}},
    {'data': {'id': 'CZ1678', 'label': 'CZ1678', 'group': 'C'}, 'position': {'x': 3100, 'y': 1500}},
    {'data': {'id': 'Z168', 'label': 'Z168', 'group': 'Z'}, 'position': {'x': 3200, 'y': 1500}},
    {'data': {'source': 'Z162', 'target': 'CZ1623'}},
    {'data': {'source': 'Z163', 'target': 'CZ1623'}},
    {'data': {'source': 'Z163', 'target': 'CZ1634'}},
    {'data': {'source': 'Z164', 'target': 'CZ1634'}},
    {'data': {'source': 'Z164', 'target': 'CZ1645'}},
    {'data': {'source': 'Z165', 'target': 'CZ1645'}},
    {'data': {'source': 'Z165', 'target': 'CZ1656'}},
    {'data': {'source': 'Z166', 'target': 'CZ1656'}},
    {'data': {'source': 'Z166', 'target': 'CZ1667'}},
    {'data': {'source': 'Z167', 'target': 'CZ1667'}},
    {'data': {'source': 'Z167', 'target': 'CZ1678'}},
    {'data': {'source': 'Z168', 'target': 'CZ1678'}},
    {'data': {'source': 'Z162', 'target': 'CZ1612'}},
]
CNOT1_edges =[{'data': {'source': 'X162', 'target': 'CX1523'}},
              {'data': {'source': 'Z152', 'target': 'CZ1623'}},]

CNOT2X = ['CX978', 'CX1078', 'CX1167', 'CX1278', 'CX1367', 'CX1456', 'CX1523']  # 按需扩展
CNOT2X_edges = [{'data': {'source': 'X83','target': target,}} for target in CNOT2X]
CNOT2Z = ['Z93', 'Z103', 'Z113', 'Z123', 'Z133', 'Z143', 'Z153']
CNOT2Z_edges = [{'data': {'source': 'CZ834','target': target,}} for target in CNOT2Z]

CNOT3X = ['CX567', 'CX656', 'CX767', 'CX1278', 'CX1367', 'CX1456', 'CX1523']  # 按需扩展
CNOT3X_edges = [{'data': {'source': 'X44','target': target,}} for target in CNOT3X]
CNOT3Z = ['Z54', 'Z64', 'Z74', 'Z124', 'Z134', 'Z144', 'Z154']
CNOT3Z_edges = [{'data': {'source': 'CZ445','target': target,}} for target in CNOT3Z]

CNOT4X = ['CX378', 'CX656', 'CX767', 'CX1078', 'CX1167', 'CX1456', 'CX1523']  # 按需扩展
CNOT4X_edges = [{'data': {'source': 'X25','target': target,}} for target in CNOT4X]
CNOT4Z = ['Z35', 'Z65', 'Z75', 'Z105', 'Z115', 'Z145', 'Z155']
CNOT4Z_edges = [{'data': {'source': 'CZ256','target': target,}} for target in CNOT4Z]

CNOT5X = ['CX378', 'CX567', 'CX767', 'CX978', 'CX1167', 'CX1367', 'CX1523']  # 按需扩展
CNOT5X_edges = [{'data': {'source': 'X16','target': target,}} for target in CNOT5X]
CNOT5Z = ['Z36', 'Z56', 'Z76', 'Z96', 'Z116', 'Z136', 'Z156']
CNOT5Z_edges = [{'data': {'source': 'CZ167','target': target,}} for target in CNOT5Z]

CNOT6X = ['CX378', 'CX567', 'CX656', 'CX978', 'CX1078', 'CX1278']  # 按需扩展
CNOT6X_edges = [{'data': {'source': 'X157','target': target,}} for target in CNOT6X]
CNOT6Z = ['Z37', 'Z57', 'Z67', 'Z97', 'Z107', 'Z127']
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
