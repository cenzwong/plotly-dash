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

# ==============================
myAlert = dbc.Alert("One of two columns", color="primary")
myHead = html.H1("Cyberport Bus ETA", style={'textAlign': 'center'})
myLayout = [
    [myHead],
    [myAlert, myAlert, myAlert],
    [card, card, card, card]
]
import pprint
def lt2app_layout(layoutss):
    _myCol = []
    _myBody = []
    for row in layoutss:
        for col in row:
            _myCol.append(dbc.Col(html.Div(col), width=12/len(row)))
    _myBody.append(dbc.Container(dbc.Row(_myCol)))
    return html.Div(children=_myBody)
app.layout = lt2app_layout(myLayout)

    
# ======================
# myRow = []
# myCol = []
# myCol.append(dbc.Col(html.Div(dbc.Alert("One of two columns", color="primary")), width=3))
# myCol.append(dbc.Col(html.Div(dbc.Alert("One of two columns", color="primary")), width=3))
# myCol.append(dbc.Col(html.Div(dbc.Alert("One of two columns", color="primary")), width=3))
# myCol.append(dbc.Col(html.Div(dbc.Alert("One of two columns", color="primary")), width=3))
# myRow.append(dbc.Row(myCol))

# myRow2 = []
# myCol2 = []
# myCol2.append(dbc.Col(html.Div(dbc.Alert("One of two columns", color="primary")), width=4))
# myCol2.append(dbc.Col(html.Div(dbc.Alert("One of two columns", color="primary")), width=4))
# myCol2.append(dbc.Col(html.Div(card), width=4))
# myRow2.append(dbc.Row(myCol2))

# body = []
# body.append(dbc.Container(html.H1("Cyberport Bus ETA", style={'textAlign': 'center'})))
# body.append(dbc.Container(myRow))
# body.append(dbc.Container(myRow2))

# app.layout = html.Div(children=body)


if __name__ == "__main__":
    app.run_server(debug=True, port=8066, host='0.0.0.0') # for debug
