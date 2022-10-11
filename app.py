import pandas as pd
import dash
import sqlite3
import plotly_express as px
from dash import html,dcc

# read the database

db = sqlite3.connect("test1.db")

query  = "select Sex,Survived as survived  from titanic"
x1 = pd.read_sql(query,db).groupby(["Sex","survived"]).size().reset_index().rename(columns = {0:"count"})
query = "select Sex from titanic"
x2 = pd.read_sql(query,db).value_counts().reset_index().rename(columns = {0:"count"})
query = "select Pclass,Fare from titanic"
x3 = pd.read_sql(query,db).groupby("Pclass")["Fare"].agg("mean").reset_index().rename(columns = {0:"count"})
fig1 = px.bar(x1,x = "survived",y = "count",color = "Sex")
fig2 = px.pie(x2,names = "Sex",values = "count")
fig3 = px.bar(x3,x = "Pclass",y = "Fare",orientation = "h")


app = dash.Dash()
app.layout = html.Div(
    children = [
        html.Div(dcc.Graph(id = "figure1",figure = fig1)),
        html.Div(dcc.Graph(id = "figure2",figure = fig2)),
        html.Div(dcc.Graph(id = "figure3",figure = fig3))
    ]
)

if __name__ == "__main__":
    app.run_server(debug = True)