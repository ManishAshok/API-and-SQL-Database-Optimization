
from flask import Flask, jsonify, request
import mysql.connector
from flask_caching import Cache

app = Flask(__name__)

# Configure Flask-Caching
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

# Database connection
def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='yourusername',
        password='yourpassword',
        database='yourdatabase'
    )
    return connection

# Get all users (with caching)
@app.route('/users', methods=['GET'])
@cache.cached(timeout=60)
def get_users():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    conn.close()
    return jsonify(users)

# Get user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM users WHERE user_id = %s', (user_id,))
    user = cursor.fetchone()
    conn.close()
    if user:
        return jsonify(user)
    else:
        return jsonify({'error': 'User not found'}), 404

# Create a new user
@app.route('/users', methods=['POST'])
def create_user():
    new_user = request.get_json()
    username = new_user['username']
    email = new_user['email']
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (username, email) VALUES (%s, %s)', (username, email))
    conn.commit()
    conn.close()
    return jsonify({'message': 'User created successfully'}), 201

# Get all transactions for a user (with pagination)
@app.route('/users/<int:user_id>/transactions', methods=['GET'])
def get_user_transactions(user_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    # Pagination parameters
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    offset = (page - 1) * per_page
    
    cursor.execute('SELECT * FROM transactions WHERE user_id = %s LIMIT %s OFFSET %s', (user_id, per_page, offset))
    transactions = cursor.fetchall()
    
    conn.close()
    return jsonify(transactions)

if __name__ == '__main__':
    app.run(debug=True)
