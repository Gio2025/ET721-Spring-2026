"""
George Athanasopoulous
March 10, 2026
Lab 11, Introduction to Flask
"""

from flask import Flask, render_template


# create an object 'app' from the flask module
app = Flask(__name__)

# set the routing to the main page
# 'route' decorator is used to access the root URL
@app.route('/')
def index():
    name = "George Athanasopoulos"
    fruits = ['apple', 'orange', 'grapes']
    fruit = 'orange' 
    return render_template('index.html', username = name, listfruits = fruits, f = fruit )

# endpoints refer to the name of the view in an app
@app.route('/about')
def about():
    return '<h1>About Us</h1>'

@app.route('/quotes')
def quotes():
    return '<h1>Quotes</h1>'

# set the 'app' to run if you execute the file directly (not when it is imported)
if __name__ == '__main__':
    app.run(debug = True)
