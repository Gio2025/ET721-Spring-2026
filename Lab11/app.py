"""
George Athanasopoulous
March 10, 2026
Lab 11, Introduction to Flask
"""

from flask import Flask, render_template

# create an object 'app' from the flask module
app = Flask(__name__)

# set the routing to the main page
@app.route('/')
def index():
    name = "George Athanasopoulos"
    fruits = ['apple', 'orange', 'grapes']
    fruit = 'orange'
    return render_template('index.html', username = name, listfruits = fruits, f = fruit )

# about page
@app.route('/about')
def about():
    images = ['mountain.jpg', 'desert.jpg', 'ocean.jpg']
    return render_template('about.html', listimages = images)

# quotes page
@app.route('/quotes')
def quotes():
    return render_template('quotes.html')

# run the app
if __name__ == '__main__':
    app.run(debug = True)