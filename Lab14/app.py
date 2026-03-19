"""
George Athanasopoulos
March 19th, 2026
Lab 14, Mini blog app using Flask
"""

from flask import Flask, render_template, redirect, url_for, request
from flask_mysqldb import MySQL

app = Flask(__name__)

# Database connection
db = mysql.connect.connect(
    host = 'localhost',
    user = 'flaskuser',
    password = 'password123',
    database = 'blogDB'
)

# Create a tool 'cursor' to be used to run querie in database
cursor = db.cursor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_blog')
def add_blog():
    username = request.form['username']
    email = request.form['email']
    title = request.form['title']
    content = request.form['content']

    # Insert into table users
    cursor.execute("INSERT INTO users(username, email) VALUES (%s, %s)", (username, email))

    db.commit()

    # Get the ID of the last row that was inserted into the database and store it in user_id
    user_id = cursor.lastrowid

    # insert data into table blog
    cursor.execut("INSERT INTO blog(user_id, title, content) VALUES(%s, %s, %s), (user_id, title, content)")

    db.commit()

    return redirect('/blogs')


@app.route('/blogs')
def blogs():
    cursor.execute("SELECT blog.id, users.username, blog.title, blog.content, blog.created_at FROM blog JOIN users ON blog.user_id = users.userid")

    # Get all the data and store them in 'data' 
    data = cursor.fetchall()

    return render_template('blogs.html', blogs = data)


if __name__ == '__main__':
    app.run(debug=True)