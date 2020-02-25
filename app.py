from flask import Flask, render_template, jsonify, after_this_request
from flask_pymongo import PyMongo

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/BinanceAPI"
mongo = PyMongo(app)

# {"test" : singledocument['open_time']}
@app.route("/API_endpoint", methods=['GET'])
def index():
    @after_this_request
    def add_header(response):
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response
    singledocument = mongo.db.XRPBTCAugKlines.find({}).limit(10)
    data = []
    for x in singledocument:
        data.append({'open_time' : x['open_time'], 'open_price' : x['open_price']})

    return jsonify(data)


@app.route("/API_endpoint")
def api_call():

    return 'Success!'


if __name__ == "__main__":
    app.run()