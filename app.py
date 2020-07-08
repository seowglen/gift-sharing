from flask import Flask, request, render_template, redirect, 
import copy
import random

app = Flask(__name__)

def secret_santa(names):
    my_list = names
    choose = copy.copy(my_list)
    result = []
    for i in my_list:
        names = copy.copy(my_list)
        names.pop(names.index(i))
        chosen = random.choice(list(set(choose) & set(names)))
        result.append((i,chosen))
        choose.pop(choose.index(chosen))
    return result


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/result", methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        names = request.form['names']
        names = names.split()
        list_names = secret_santa(names)
        return render_template('result.html', list_names=list_names)
