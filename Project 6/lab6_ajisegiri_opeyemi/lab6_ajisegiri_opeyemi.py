"""
A lab programme that highlights flask framework
Author: Opeyemi Ajisegiri
Class: SDEV 300
Assignment: Lab 6
"""

from datetime import datetime
from flask import Flask
from flask import render_template

app= Flask(__name__)


#the_date = datetime.now()
#today = the_date.strftime("%B %d, %Y  %H:%M:%S ")

@app.route('/')
#@app.route('/<today>')
#Commented out to avoid any lingering security issues.
def index():
    """  Rendering the homepage """
    the_date = datetime.now()
    today = the_date.strftime("%B %d, %Y  %H:%M:%S ")
    return render_template('index.html', today=today)


@app.route('/about')
def about():
    """ Rendering the About papge """
    return render_template('about.html')

@app.route('/project')
def project():
    """ Rendering the Project papge """
    return render_template('project.html')

@app.route('/contact')
def contact():
    """ Rendering the Contact papge """
    return render_template('contact.html')
