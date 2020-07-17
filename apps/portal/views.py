from django.shortcuts import render
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math
import io
import urllib, base64
from . import data

def truncate(number, digits) -> float:
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper

def func(label, pct, allvalues):
    absolute = pct * 100/np.sum(allvalues)
    return "{}\n{}%".format(label, truncate(absolute,2))


def home(request):
    results_df = data.getDataframe()
    print(len(results_df.index))

    explode = (0.0, 0.0, 0.1, 0.1, 0.1, 0.1)
    labels = pd.unique(results_df['Estado'])
    labels_with_percentage = []

    estados = []

    for label in labels:
       sum = (results_df.Estado == label).sum()
       estados.append(sum)

    for (label, estado) in zip(labels,estados):
       labels_with_percentage.append(func(label, estado, estados))

    fig, ax = plt.subplots(figsize = (10, 7))

    ax.pie(estados, explode=explode, labels=labels,  startangle=180)

    plt.axis('equal') # Try commenting this out.
    plt.title('Estado Contagiados Covid En Colombia')
    plt.legend(labels_with_percentage, loc='center', bbox_to_anchor=(0, 1),
              fontsize=12)

    #plt.plot(range(10))
    #fig = plt.gcf()
    buf = io.BytesIO()
    plt.savefig(buf, format = 'png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)
    return render(request, 'home.html', {'data':uri})
