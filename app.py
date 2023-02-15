from flask import Flask, render_template, request, redirect, flash, url_for
import sqlite3
import os

currentdirectory = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/Users/<id>')
def get_user_packages(id):
    conn = get_db_connection()
    packages = conn.execute('SELECT * FROM Packages WHERE user_id = ?' (id,))
    conn.close()
    return render_template('Packages.html', packages=packages)
    
@app.route('/')
def main():
    return render_template("Index.html")

@app.route('/SignUp', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if not email:
            flash('email is required!')
        elif not password:
            flash('Content is required!')
            
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO Users (email, password) VALUES (?, ?)',
                         (email, password))
            conn.commit()
            conn.close()
            '''id = conn.execute('SELECT id FROM Users WHERE email = ?', (email,))
            conn.close() '''
            #return redirect(url_for('get_user_packages', id=id))
            return redirect(url_for('main'))

    return render_template('SignUp.html')
