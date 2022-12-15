"""
A lab programme that builds the web application for a company using
     the python based flask framework.
Author: Opeyemi Ajisegiri
Class: SDEV 300
Assignment: Lab 7
"""

import os
import re
from flask import Flask,redirect,url_for,request,flash,session
from flask import render_template
from passlib.hash import sha256_crypt

app= Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def index():
    """  Rendering the homepage """
    return render_template('index.html')

@app.route('/about')
def about():
    """ Rendering the About papge """
    return render_template('about.html')

@app.route('/idea')
def idea():
    """ Rendering the Ideas page """
    return render_template('idea.html')

@app.route('/contact')
def contact():
    """ Rendering the Contact papge """
    return render_template('contact.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    """ Rendering the User Registration page
         and post the user info int the file """
    if request.method == "POST":
        firstname = request.form["firstname"]
        lastname = request.form["lastname"]
        email = request.form["email"]
        password = request.form["password"]
        error = None
        if not any(p.islower() for p in password):
            error = """Password must have small and capital letters,
                        numbers , and special characters"""
        elif not any(p.isupper() for p in password):
            error = """Password must have small and capital letters,
                        numbers , and special characters"""
        elif not any(p.isdigit() for p in password):
            error = """Password must have small and capital letters,
                        numbers , and special characters"""
        elif not re.search("(?=.*[@#$])",password):
            error = """Password must have small and capital letters,
                       numbers , and special characters"""
        elif len(password) < 12:
            error = "Password must have at least 12 characters"
        user = {"fname":"","lname":"","email":"","pword":""}
        with open('file.txt', "r") as file:
            for record in file:
                user["fname"],user["lname"],user["email"],user["pword"] = record.split(' ')
                if user["email"] == email:
                    error = """The email has already been registered,
                                would you rather log in?"""
        flash(error)
        if error is None:
            with open('file.txt', "a") as file:
                hash_pass = sha256_crypt.hash(password)
                new_record =' '.join([firstname,lastname,email,hash_pass])
                file.write(new_record)
                file.write('\n')
                session['name'] = firstname
            return redirect(url_for("blog", name=firstname))
    return render_template('registration.html')

@app.route('/sign_out')
def sign_out():
    """ Signing user out of the application"""
    session.pop('name')
    return redirect(url_for('index'))

@app.route('/blogging')
def blog():
    """ Rendering the blogging page after the user
        has been signed. """
    if 'name' not in session:
        error = "Please sign in"
        flash(error)
        return redirect(url_for('login'))
    return render_template('blogging.html',name=session['name'])


@app.route('/login', methods=["GET","POST"])
def login():
    """ Render the user login page
        and comparing the input with values in the file """
    error = None
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        #hash_pass = sha256_crypt.hash(password)
        user = {"fname":"","lname":"","email":"","pword":""}
        with open('file.txt', "r") as file:
            for record in file:
                user["fname"],user["lname"],user["email"],user["pword"] = record.split(' ')
            if email == user["email"] and sha256_crypt.verify(password, user["pword"]):
                session['name'] = user["fname"]
                return redirect(url_for('blog', name=user["fname"]))
            else:
                error = "email or password not found"
        flash(error)
    #if error == None:
    #    return redirect(url_for('blogging'))
    #else:
    #    return render_template("login.html", error = error)
    return render_template('login.html')
