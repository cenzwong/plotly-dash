# https://medium.com/swlh/dashboards-in-python-for-beginners-using-dash-responsive-mobile-dashboards-with-bootstrap-css-2a0d05a53cf6

import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

card = dbc.Card(
    [
        dbc.CardImg(src="https://images.theconversation.com/files/319652/original/file-20200310-61148-vllmgm.jpg?ixlib=rb-1.1.0&q=45&auto=format&w=754&fit=clip", top=True),
        dbc.CardBody(
            [
                html.H4("Card title", className="card-title"),
                html.P(
                    "Some quick example text to build on the card title and "
                    "make up the bulk of the card's content.",
                    className="card-text",
                ),
                dbc.Button("Go somewhere", color="primary"),
            ]
        ),
    ],
    style={"width": "18rem"},
)

# class myLayout:
#     _nCol = 0
#     _myRow = []

#     def __init__(self, nCol):
#         self._nCol = nCol
    
#     def appendRow(self, ltDBC, ltWidth):
#         myCol = []
#         for ltdbc, ltwidth in zip(ltDBC, ltWidth):
#            myCol.append(dbc.Col(html.Div(ltdbc), width=ltwidth))
#         self._myRow.append(dbc.Row(myCol))
    
#     def appendBody(self, ltHtml):
#         myBody = []
#         for lthtml in ltHtml:
#            myBody.append(dbc.Container(lthtml))
#         for myR in self._myRow:
#            myBody.append(dbc.Container(myR))
#         return html.Div(children=myBody)

# myLay = myLayout(4)
# myLay.appendRow([dbc.Alert("One of two columns", color="primary"),
#         dbc.Alert("One of two columns", color="primary"),
#         dbc.Alert("One of two columns", color="primary")], [4,4,4])
# myLay.appendRow([card, card, card, card], [3,3,3,3])
# app.layout = myLay.appendBody([html.H1("Cyberport Bus ETA", style={'textAlign': 'center'})])
# ======================
myRow = []
myCol = []
myCol.append(dbc.Col(html.Div(dbc.Alert("One of two columns", color="primary")), width=3))
myCol.append(dbc.Col(html.Div(dbc.Alert("One of two columns", color="primary")), width=3))
myCol.append(dbc.Col(html.Div(dbc.Alert("One of two columns", color="primary")), width=3))
myCol.append(dbc.Col(html.Div(dbc.Alert("One of two columns", color="primary")), width=3))
myRow.append(dbc.Row(myCol))

myRow2 = []
myCol2 = []
myCol2.append(dbc.Col(html.Div(dbc.Alert("One of two columns", color="primary")), width=4))
myCol2.append(dbc.Col(html.Div(dbc.Alert("One of two columns", color="primary")), width=4))
myCol2.append(dbc.Col(html.Div(card), width=4))
myRow2.append(dbc.Row(myCol2))

body = []
body.append(dbc.Container(html.H1("Cyberport Bus ETA", style={'textAlign': 'center'})))
body.append(dbc.Container(myRow))
body.append(dbc.Container(myRow2))

app.layout = html.Div(children=body)


if __name__ == "__main__":
    app.run_server(debug=True, port=8066, host='0.0.0.0') # for debug
