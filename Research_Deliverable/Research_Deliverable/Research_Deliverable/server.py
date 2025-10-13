# flask --app data_server run

from flask import Flask
from flask import render_template
from flask import request
import json


app = Flask(__name__, static_url_path='', static_folder='static')


@app.route('/')
def about():
    return render_template("about.html")

@app.route('/introduction')
def introduction():  
    return render_template("introduction.html")

@app.route('/results')
def results():  
    return render_template("results.html")

@app.route('/discussion')
def discussion():  
    return render_template("discussion.html")

@app.route('/annotated_bib')
def annotated_bib():  
    return render_template("annotated_bib.html")


if __name__ == "__main__":
    app.run(debug=True)

