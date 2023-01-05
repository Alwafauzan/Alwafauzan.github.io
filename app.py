# from crypt import methods
from operator import mod
from flask import Flask, request
from flask import Flask, render_template
import joblib
# import sklearn
# from sklearn.neighbors import KNeighborsClassifier
import numpy as np
app = Flask(__name__)

@app.route("/" , methods=['POST','get'])
def index():
    return "hai"

if __name__ == "__main__":
    app.run(debug=True)
