from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_mysqldb import MySQL
from flask_bcrypt import Bcrypt
from config import Config

app = Flask(__name__)

#-------------------------------
# Loading Page
#-------------------------------
@app.route('/')
def home():
    return redirect(url_for('login'))


#-------------------------------
# Login Routing
#-------------------------------
@app.route('/login')
def login():

    return render_template('login.html')


#-------------------------------
# Signup Routing
#-------------------------------
@app.route('/singup')
def signup():
    return render_template('signup.html')


#-------------------------------
# Run App
#-------------------------------
if __name__ == '__main__':
    app.run(debug=True)