import pandas as pd
from flask import Flask
app = Flask(__name__)

@app.route("/")
def helloo():
    df=pd.read_csv("airtravel.csv",doublequote=False)
    return df.to_html()
if__name__=="__main__":
    app.run()
