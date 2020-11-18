# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

# for all those graph: https://plotly.com/python/pie-charts/

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import base64
#====================================
from pymongo import MongoClient
import pprint as pp


URL = base64.b64decode('MSBD5003bW9uZ29kYjovL21zYmQ1MDAzLW1vbmdvZGI6enNFVGlXRGFBSmRxT0RmT2c2Mm1pcGxTOWtITUVzNU41eGhtZ3lJelN6RWFPS1ZmTWRKcDdJVVRoQnFkN29iSzFPQnNuUjFuMmhIcU1kT1JNQ0N4Nnc9PUBtc2JkNTAwMy1tb25nb2RiLm1vbmdvLmNvc21vcy5henVyZS5jb206MTAyNTUvP3NzbD10cnVlJnJlcGxpY2FTZXQ9Z2xvYmFsZGImcmV0cnl3cml0ZXM9ZmFsc2UmbWF4SWRsZVRpbWVNUz0xMjAwMDAmYXBwTmFtZT1AbXNiZDUwMDMtbW9uZ29kYkA=')
URL_Mongo = str(URL)[2:-1]
client = MongoClient(URL_Mongo)

db_credit = client['credit']
db_credit_application = db_credit['application']
#===========================================


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
# ======================
application_Male = db_credit_application.count_documents({"CODE_GENDER": "M"})
application_Female = db_credit_application.count_documents({"CODE_GENDER": "F"})
labels = ['Male','Female']
values = [application_Male, application_Female]
# values = [44776, 44778]
fig1 = go.Figure(data=[go.Pie(labels=labels, values=values)])

# ======================
application_Cash_loans = db_credit_application.count_documents({"NAME_CONTRACT_TYPE": "Cash loans"})
application_Revolving_loans = db_credit_application.count_documents({"NAME_CONTRACT_TYPE": "Revolving loans"})

labels = ['Cash loans','Revolving_loans']
values = [application_Cash_loans, application_Revolving_loans]
# values = [44776, 44778]
fig2 = go.Figure(data=[go.Pie(labels=labels, values=values)])

# ======================
results = list(db_credit_application.find({'CODE_GENDER': 'M', 'AMT_ANNUITY':{'$gt':100,'$lt':150000}}, {'AMT_ANNUITY':1, '_id':0}))
myX = [myDict["AMT_ANNUITY"] for myDict in results]

fig3 = go.Figure(data=[go.Histogram(x=myX, histnorm='probability')])
# ======================
pipeline = [
    {"$group": {"_id": "$NAME_INCOME_TYPE", "count": {"$sum": 1}}}
]
results = list(db_credit_application.aggregate(pipeline))
pp.pprint(results)
labels = [myDict["_id"] for myDict in results]
values = [myDict["count"] for myDict in results]

fig4 = go.Figure(data=[go.Pie(labels=labels, values=values)])
# ======================
app.layout = html.Div(children=[
    html.H1(children='Home Credit Default Risk'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='application_male_female',
        figure=fig1
    ),

    dcc.Graph(
        id='contract_type_distribution',
        figure=fig2
    ),

    dcc.Graph(
        id='Histogram_of_Annuinity',
        figure=fig3
    ),

    dcc.Graph(
        id='Ratio Income Type',
        figure=fig4
    ),

])

if __name__ == '__main__':
    # app.run_server(debug=True, port=8050, host='0.0.0.0')
    app.run_server(debug=False, port=8050)










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


