from flask import Flask,render_template, request, redirect,url_for, flash, session
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # for sessions and flash messages

# MySQL Database Configuration
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="partha",
    database="hospital_db"
)
cursor = db.cursor(dictionary=True)

@app.route('/')
def home():
    return render_template('login.html')  # same as your HTML

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    query = "SELECT * FROM users WHERE email=%s AND password=%s"
    cursor.execute(query, (email, password))
    user = cursor.fetchone()

    if user:
        session['user'] = user['email']
        flash('Login successful!', 'success')
        return redirect(url_for('dashboard'))
    else:
        flash('Invalid credentials, try again.', 'danger')
        return redirect(url_for('home'))

@app.route('/dashboard')
def dashboard():
    if 'user' in session:
        return f"Welcome to the dashboard, {session['user']}!"
    else:
        return redirect(url_for('home'))

@app.route('/logout')
def logout():
    session.pop('user', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)