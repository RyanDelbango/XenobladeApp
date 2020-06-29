# ./python_code/api.py
import os
import pickle
from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
import numpy as np
from Blade import Blade
app = Flask(__name__)
CORS(app)
api = Api(app)
@app.route("/")                 
def BladeList():
    y = Blade("Pyra", "Fire")       
    return y.name
if __name__ == "__main__":
    app.run() 
app.run(debug=True)