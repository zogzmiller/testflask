from flask import Flask, render_template, jsonify, after_this_request
from flask_pymongo import PyMongo
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
import pandas as pd


app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/fruits_db"
mongo = PyMongo(app)

# SQLAlchemy Setup
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/shark.sqlite"
# db = SQLAlchemy(app)

# Base = automap_base()

# Base.prepare(db.engine, reflect=True)

# shark_data_cleaned = Base.classes.shark_data_cleaned

@app.route("/")
def api_call():

    return render_template('index.html')



@app.route("/API_endpoint", methods=['GET'])
def index():
    singledocument = mongo.db.fruits_db.find({})
    data = []
    for x in singledocument:
        data.append({'vendor' : x['vendor'], 'fruit' : x['fruit'], 'quantity' : x['quantity']})

    return jsonify(data)





if __name__ == "__main__":
    app.run()