import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib import colors
# from PIL import Image
import pandas as pd
import collections
from linecache import getline

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_samples, silhouette_score

import seaborn as sn

# %matplotlib inline
# matplotlib.rcParams['figure.figsize'] = (15.0, 8.0)
# img = plt.imread('./testdata/awe43d11feb16/AW-NE43D-099-059A-11Feb16-BAND1.tif')
# plt.imshow(img[:, :])
# plt.show()

import numpy as np
import pickle
import requests
from flask import Flask, render_template


app = Flask(__name__, template_folder='./')


def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1, 12)
    loaded_model = pickle.load(open("model.pkl", "rb"))
    result = loaded_model.predict(to_predict)
    print(str(round(result[0]/10, 2)))
    return str(round(result[0]/10, 2))


def hello_world():
    # input Data for test here =>
    # to_predict_list = [1] * 24

    to_predict_list = [8.60, 8.60, 8.10, 8.20, 8.30, 8.40, 8.60, 8.30, 8.40, 8.60, 8.60, 8.60, 8.60, 8.60, 8.60, 8.60, 8.60, 8.60, 8.60, 8.60, 8.60, 8.60, 8.60, 8.60]
    print(to_predict_list)
    to_predict = np.array(to_predict_list).reshape(1, 1, 24)
    print(to_predict)
    loaded_model = pickle.load(open("../filename.pkl", "rb"))
    result = loaded_model.predict(to_predict)
    result = str(result[0][0] * 100)
    print(result)
    return round(float(result), 2)


def style():
    return render_template("./style.css")

app.add_url_rule('/styles', 'styles.css', style);

@app.route("/dashboard")

def dashboard():
    return render_template("index.html", val = hello_world())



if __name__ == '__main__':
    app.run(debug=True)
