import numpy.random as rnd
import time
import json
import flask
from flask import Flask

app = Flask(__name__)

def random_wait():
    return rnd.normal(3, 2)

@app.route("/ping")
def ping():
    wait = random_wait()
    time.sleep(wait)

    resp = flask.Response(json.dumps({
        "msg": "pong"
    }))
    resp.headers['X-Time'] = "{:.2f}".format(wait)
    resp.headers['Content-Type'] = 'application/json'
    
    return resp 

