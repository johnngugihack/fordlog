from flask import Flask, request, jsonify
import pymysql
from flask_cors import CORS
import os
from dotenv import load_dotenv


app = Flask(__name__)
CORS(app)

# Load environment variables from the .env file
load_dotenv()

# Get credentials from environment variables
host = os.getenv('DB_HOST')
user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
database = os.getenv('DB_DATABASE')

# MySQL DB Configuration
db_config = {
    'host': host,
    'user': user,
    'password': password,
    'database': database
}
@app.route('/')
def home():
    return "Welcome to Stafford!"
@app.route('/api/register', methods=['POST'])  # Changed to 'register' to match purpose
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'success': False, 'message': 'Username and password are required'}), 400

    try:
        connection = pymysql.connect(**db_config)
        cursor = connection.cursor()

        # Insert user into login table
        query = "INSERT INTO users (username, password) VALUES (%s, %s)"
        cursor.execute(query, (username, password))
        connection.commit()

        cursor.close()
        connection.close()

        return jsonify({'success': True, 'message': 'User registered successfully'}), 201

    except Exception as e:
        print("Database error:", str(e))
        return jsonify({'success': False, 'message': 'Server error'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0' , port=5000)
