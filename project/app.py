# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

#====================================
from pymongo import MongoClient
import pprint as pp

URL_Mongo = ''
client = MongoClient(URL_Mongo)

# Accessing Database
print(client.list_database_names())
db_credit = client['credit']
#===========================================


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "x": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "y": [4, 1, 2, 2, 4, 5],
})
fig = px.bar(df, x="x", y="y")

df2 = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})
fig2 = px.bar(df2, x="Fruit", y="Amount", color="City", barmode="group")

df = px.data.gapminder().query("year == 2007").query("continent == 'Europe'")
df.loc[df['pop'] < 2.e6, 'country'] = 'Other countries' # Represent only large countries
fig = px.pie(df, values='pop', names='country', title='Population of European continent')
fig.show()


app.layout = html.Div(children=[
    html.H1(children='Home Credit Default Risk'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    ),

])

if __name__ == '__main__':
    # app.run_server(debug=True, port=8050, host='0.0.0.0')
    app.run_server(debug=True, port=8050)










# # Collection - application
# print(db_credit.list_collection_names())
# db_credit_application = db_credit['application']

# pp.pprint(db_credit_application.count_documents({}))

# documents = db_credit_application.find({"NAME_CONTRACT_TYPE" : "Revolving loans"})
# pp.pprint(documents[0])

# pp.pprint(db_credit_application.count_documents({"NAME_CONTRACT_TYPE" : "Revolving loans"}))

# db_credit_application.distinct("CODE_GENDER")

# # Collection - installment
# print(db_credit.list_collection_names())
# db_credit_installment = db_credit['installment']

# documents = db_credit_installment.find({})
# pp.pprint(documents)

# # Collection - prev_application
# print(db_credit.list_collection_names())
# db_credit_prev_application = db_credit['prev_application']

# documents = db_credit_prev_application.find({})
# pp.pprint(documents[0])
# pp.pprint(db_credit_prev_application.find_one())


