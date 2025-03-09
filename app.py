from flask import Flask, jsonify, request, render_template, redirect, url_for
import sqlite3
from flask_login import LoginManager, login_user, login_required, current_user, logout_user, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'test'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login_page"  # Redirect unauthorized users to login


class User(UserMixin):
    def __init__(self, id, username):
        self.id = id
        self.username = username


class Expense():
    def __init__(self, id, description, amount, timestamp, user_id):
        self.id = id
        self.description = description
        self.amount = amount
        self.timestamp = timestamp
        self.user_id = user_id


@login_manager.user_loader
def load_user(user_id):
    """Loads the user by ID from the database."""
    conn = sqlite3.connect('expense-track.db')
    cur = conn.execute('SELECT id, username FROM users WHERE id = ?', (int(user_id),))
    user_row = cur.fetchone()
    conn.close()
    return User(id=user_row[0], username=user_row[1]) if user_row else None


@app.route('/')
def home():
    """Home Page with Navigation Links"""
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    """Handles both GET (show login form) and POST (authenticate user)."""
    if request.method == 'GET':
        return render_template('login.html')

    if request.method == 'POST':
        data = request.json
        username = data.get('username')
        password = data.get('password')

        conn = sqlite3.connect('expense-track.db')
        cur = conn.execute('SELECT id, username, password_hash FROM users WHERE username = ?', (username,))
        user_row = cur.fetchone()
        conn.close()

        if user_row and check_password_hash(user_row[2], password):
            user = User(id=user_row[0], username=user_row[1])
            login_user(user)
            return jsonify({"status": "logged_in"}), 200

        return jsonify({"status": "error", "message": "Invalid credentials"}), 401


@app.route('/dashboard')
@login_required
def dashboard():
    """Dashboard with navigation links."""
    return render_template('dashboard.html')


@app.route('/tip-calculator')
@login_required
def tip_calculator():
    """Tip Calculator Page"""
    return render_template('tips_calculator.html')


@app.route('/expense-tracker')
@login_required
def expense_tracker():
    """Expense Tracker Page"""
    return render_template('expense_tracker.html')


@app.route('/expenses/add', methods=['POST'])
@login_required
def add_expense():
    """Add a new expense for the logged-in user."""
    data = request.json
    description = data.get('description')
    amount = data.get('amount')

    if not description or amount is None:
        return jsonify({"status": "error", "message": "Invalid input"}), 400

    conn = sqlite3.connect('expense-track.db')
    cur = conn.cursor()
    cur.execute('INSERT INTO expenses (description, amount, user_id) VALUES (?, ?, ?)',
                (description, amount, current_user.id))
    conn.commit()
    conn.close()

    return jsonify({"status": "expense_added"}), 201


@app.route('/expenses/load', methods=['GET'])
@login_required
def load_expenses():
    """Fetch all expenses for the logged-in user."""
    conn = sqlite3.connect('expense-track.db')
    cur = conn.cursor()
    cur.execute('SELECT id, description, amount, created_at, user_id FROM expenses WHERE user_id = ?', (current_user.id,))
    expenses = cur.fetchall()
    conn.close()

    # Convert each row to a dictionary
    expense_list = [{"id": row[0], "description": row[1], "amount": row[2], "timestamp": row[3], "user_id": row[4]}
                    for row in expenses]

    return jsonify({"data": expense_list}), 200


@app.route('/split-bill', methods=['GET'])
def split_bill():
    """Home Page with Navigation Links"""
    return render_template('split_bill.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login_page'))
