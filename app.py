import pandas as pd
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    df=pd.read_csv('/tmp/8d9365fa04e1064/airtravel.csv')
    return df.to_html()
