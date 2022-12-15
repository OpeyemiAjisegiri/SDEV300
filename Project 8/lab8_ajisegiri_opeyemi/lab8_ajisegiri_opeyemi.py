"""
A lab programme that builds the web application for a company using
     the python based flask framework.
Author: Opeyemi Ajisegiri
Class: SDEV 300
Assignment: Lab 8
"""

import os
import re
import logging
import pandas as pd
from flask import Flask,redirect,url_for,request,flash,session
from flask import render_template
from passlib.hash import sha256_crypt

app= Flask(__name__)
app.secret_key = os.urandom(24)

logging.basicConfig(filename="serverrecord.log", level=logging.DEBUG,
                    format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

@app.route('/')
def index():
    """  Rendering the homepage """
    if 'name' in session:
        app.logger.warning("Sign In Attempt without Valid Credentials")
        return redirect(url_for("blog", name=session['name']))
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
        #error = None
        #if not any(p.islower() for p in password):
        #    error = """Password must have small and capital letters,
        #                numbers , and special characters"""
        #elif not any(p.isupper() for p in password):
        #    error = """Password must have small and capital letters,
        #                numbers , and special characters"""
        #elif not any(p.isdigit() for p in password):
        #    error = """Password must have small and capital letters,
        #                numbers , and special characters"""
        #elif not re.search("(?=.*[@#$])",password):
        #    error = """Password must have small and capital letters,
        #               numbers , and special characters"""
        #elif len(password) < 12:
        #    error = "Password must have at least 12 characters"
        error = password_check(password)
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
            #app.logger.info("Redirected to blogging page after saving user details")
            return redirect(url_for("blog", name=firstname))
    return render_template('registration.html')

def password_check(password):
    """ Checking the strength and complexity of the password entered."""
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
    return error

@app.route('/sign_out')
def sign_out():
    """ Signing user out of the application"""
    session.pop('name')
    app.logger.info("Signed out")
    return redirect(url_for('index'))

@app.route('/blogging')
def blog():
    """ Rendering the blogging page after the user
        has been signed. """
    if 'name' not in session:
        error = "Please sign in"
        flash(error)
        app.logger.warning("Blogging page attempt without valid credentials")
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
            error = "email or password not found"
        flash(error)
    return render_template('login.html')

@app.route('/update', methods=["GET","POST"])
def update():
    """ Updating a user's password """
    error = None
    if 'name' not in session:
        error = "Please sign in"
        flash(error)
        app.logger.warning("Update action attempt without valid credentials")
        return redirect(url_for('login'))
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        with open("CommonPassword.txt","r") as pcheck:
            for record in pcheck:
                if password in record:
                    error = "Your new password is weak and insecure"
                    break;
        error = password_check(password)
        if error == None:
            frame = pd.read_csv('file.txt', sep=" ")
            #The line above seems to work just as 'pd.read_csv('file.txt')
            #with or without the file being open and pylint raises an used
            #variable flag for 'file'. 'sep=" "' added to accomodate the sepration by " "
            for index in frame.index:
                if frame.loc[index,'Email'] == email:
                    frame.loc[index,'Password'] = sha256_crypt.hash(password)
            frame.to_csv('file.txt', index=False, sep=" ")
            return redirect(url_for("blog", name=session['name']))
        flash(error)
    app.logger.info("Password Update page rendered")
    return render_template('update.html')   #, name=session['name'])
    #return redirect(url_for('update', name=session['name']))
