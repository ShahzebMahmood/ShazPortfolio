from pydoc import doc, render_doc
from click import open_file
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from sqlalchemy import databases
import sqlalchemy
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__, template_folder='template')
Bootstrap(app)

app.secret_key = "jsabcjibasuifiusahfiuh ajbdiuhasu 9u9h3"


db =SQLAlchemy()
SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'

@app.route('/Home')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/workexp')
def resume():
    return render_template('workexp.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__=='__main__':
    app.run(debug=True,port=7000)



