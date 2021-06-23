import pandas as pd
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    df=pd.read_csv("airtravel.csv")
    return df.to_html()
if__name__=="__main__":
    app.run()
