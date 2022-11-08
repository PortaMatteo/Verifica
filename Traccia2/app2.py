from flask import Flask, render_template, request,redirect,url_for,Response,url_for,redirect
app = Flask(__name__)


import io
# collegamento al database
import pandas as pd
import pymssql

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

matplotlib.use('Agg')
conn = pymssql.connect(server ='213.140.22.237\SQLEXPRESS',user='ghebrous.davide',password='xxx123##',database='ghebrous.davide')

@app.route('/', methods = ['GET'])
def home():
    return redirect(url_for('infoUser'))

@app.route('/infoUser', methods = ['GET'])
def infoUser():
    return render_template("home2.html")


@app.route('/ricerca', methods = ['GET'])
def search():
    global nome_client,cogn_client
    nome_client = request.args['fn_client']
    cogn_client = request.args['ln_client']
    query = f"select * from sales.customers where sales.customers.first_name = '{nome_client}' and sales.customers.last_name = '{cogn_client}'"
    df_client = pd.read_sql(query,conn)
    print(df_client)
    if  df_client.values.tolist() == []:
         return render_template('error2.html')
    else:
        return render_template('result2.html', nomiColonne = df_client.columns.values, dati = list(df_client.values.tolist()))


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)