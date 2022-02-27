from crypt import methods
from fileinput import close, filename
from gzip import _OpenTextMode
from logging.config import fileConfig
from msilib.schema import File
from pyexpat import model
from select import select
from statistics import mode
from click import command
from flask import Flask, redirect, GET, POST, render_template
import os
from __init__ import app
import webbrowser


@app.route("/resume", method = ['POST', 'GET'])
def load_cv():
     f = filename("/users/smahmood/Web_project/Shahzeb+Resume (1)")
     open(f, 'r')
     f.close
     return render_template("reume.html")

@app.route("/index")
def b_home():
   # name = "Shahzeb Mahmood"
   # location = "Toronto, Ontario"
    #linkedin = ""
    #git_hub_link = ""
    

    pass
@app.route("/aboutme")
def b_about_me():
    #summary = "A skilled and mature professional who enjoys the challenge of an innovative environment to achieve goals individually and within a team. Skilled in many areas working within various IT functions be it Support, Developing, Networking, Cyber Security or Telephony Solutions. "
    #work_exp = ""

    pass

