"""
George Athanasopoulos
March 19th, 2026
Lab 14, Mini blog app using Flask
"""

from flask import Flask, render_template, redirect, url_for, request
from flask_mysqldb import MySQL

app = Flask(__name__)

# Database connection
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'flaskuser'
app.config['MYSQL_PASSWORD'] = 'password123'
app.config['MYSQL_DB'] = 'blogDB'

mysql = MySQL(app)

# Create a tool 'cursor' to be used to run queries in database

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/addblog', methods=['POST'])
def addblog():
    username = request.form['username']
    email = request.form['email']
    title = request.form['title']
    content = request.form['content']

    cursor = mysql.connection.cursor()

    # Insert into table users
    cursor.execute("INSERT INTO users(username, email) VALUES (%s, %s)", (username, email))
    mysql.connection.commit()

    # Get last inserted id
    userid = cursor.lastrowid

    # insert data into table blog
    cursor.execute(
        "INSERT INTO blog(user_id, title, content) VALUES (%s, %s, %s)",
        (userid, title, content)
    )
    mysql.connection.commit()

    return redirect(url_for('blogs'))

@app.route('/blogs')
def blogs():
    cursor = mysql.connection.cursor()

    cursor.execute("SELECT blog.id, users.username, blog.title, blog.content, blog.created_at FROM blog JOIN users ON blog.user_id = users.userid")

    data = cursor.fetchall()

    return render_template('blogs.html', blogs=data)

if __name__ == '__main__':
    app.run(debug=True)