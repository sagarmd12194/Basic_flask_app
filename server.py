from builtins import print
from flask import Flask, render_template, redirect, request
import csv

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def index(page_name=None):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit(page_name=None):
    if request.method == 'POST':
        data = request.form.to_dict()
        name = data['name']
        message = data['message']

        with open("database.csv", "a", newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow([name, message])

        with open("database.txt", "a") as file:
            file.write("\n"+name+"\t"+message)


    else:
        print("This is not post request")
    return redirect("/thank_you.html")
