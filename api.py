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
    y = Blade("Pyra", "Fire", "https://vignette.wikia.nocookie.net/xenoblade/images/e/ee/Pyra_pic.png/revision/latest/top-crop/width/360/height/360?cb=20170712045817") 
    return {("Blade": str(y.name)), ("Picture": str(y.Picture))}
if __name__ == "__main__":
    app.run() 
app.run(debug=True)