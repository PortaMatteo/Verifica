from flask import Flask, render_template, request, Response
app = Flask(__name__)

import io
import pandas as pd 
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib
matplotlib.use('Agg')
import pymssql

conn = pymssql.connect(server='213.140.22.237\SQLEXPRESS', user='porta.matteo', password='xxx123##', database='porta.matteo')

@app.route("/", methods=["GET"])
def home():
    return render_template("home4.html")

@app.route("/ricerca", methods=["GET"])
def ricerca():
    idCliente = request.args["id"]
    query = f"SELECT * FROM sales.customers WHERE customers.customer_id = {idCliente}"
    tabella = pd.read_sql(query, conn)
    return render_template("informazioni.html", nomiColonne = tabella.columns.values, dati = tabella.values)



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)