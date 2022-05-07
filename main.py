from flask import Flask, request, redirect, render_template, jsonify
import time
import os
import json



app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')


@app.route('/bmi_calculator', methods=['GET', 'POST'])
def bmi():
    return render_template('bmi.html')

if __name__ == "__main__":
    app.run(debug=True)

