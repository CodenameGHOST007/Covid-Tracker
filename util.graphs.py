import urllib
from utils import paginator, api_covid
from operator import itemgetter
import matplotlib.pyplot as plt
from io import BytesIO,FileIO
import os
from datetime import datetime
import json
import random
import time
import requests
def send_error(s):
    print(s)
def plot_graph_logrythmic_country(iso3, num, name):
    data = api_covid.CovidAPI().get_country_timeline1(iso3)
    if data is None:
        send_error("API Error!")
        return
    x_axis = []
    cases = []
    deaths = []
    recovery = []
    for x in data['result']:
        try:
            x_axis.append(datetime.strptime(str(x), '%Y-%m-%d'))
            cases.append(data['result'][x]['confirmed'])
            deaths.append(data['result'][x]['deaths'])
            recovery.append(data['result'][x]['recovered'])
        except Exception:
            pass
    plt.plot(x_axis, cases, color='yellow', linestyle='-', marker='o', markersize=4, markerfacecolor='yellow', label="Total Cases")
    plt.plot(x_axis, recovery, color='green', linestyle='-', marker='o', markersize=4, markerfacecolor='green', label="Total Recoveries")
    plt.plot(x_axis, deaths, color='red', linestyle='-', marker='o', markersize=4, markerfacecolor='red', label="Total Deaths")

    plt.gcf().autofmt_xdate()
    plt.grid()
    plt.legend()
    ax = plt.axes()
    plt.setp(ax.get_xticklabels(), color="white")
    plt.setp(ax.get_yticklabels(), color="white")
    filename = "%s.png" % str(random.randint(0,9090909090))
    plt.savefig(filename, transparent=True)
    

    #display file

    os.remove(filename)
    plt.clf()
    plt.close()


def plot_graph_linear_country(ctx, iso3, name):
    data = api_covid.CovidAPI().get_country_timeline1(iso3[0])
    if data is None:
        send_error("API Error!")
        return
    x_axis = []
    cases = []
    for x in data['result']:
        try:
            x_axis.append(datetime.strptime(str(x), '%Y-%m-%d'))
        except Exception:
            pass
    for x in iso3:
        data = api_covid.CovidAPI().get_country_timeline1(x)
        if data is None:
            send_error("API Error!")
            return
        arr = []
        for y in data['result']:
            try:
                arr.append(data['result'][y]['confirmed'])
            except Exception:
                pass
        cases.append(arr)
    col = ["red", "orange", "green", "blue", "yellow"]
    for i in range(0, len(iso3)):
        plt.plot(x_axis, cases[i], color=col[i], linestyle='-', marker='o', markersize=4, markerfacecolor=col[i],
                 label=name[i])

    plt.gcf().autofmt_xdate()
    plt.grid()
    plt.legend()
    ax = plt.axes()
    plt.setp(ax.get_xticklabels(), color="white")
    plt.setp(ax.get_yticklabels(), color="white")
    filename = "%s.png" % str(ctx.message.id)
    plt.savefig(filename, transparent=True)

    #add image

    os.remove(filename)
    plt.clf()
    plt.close()

