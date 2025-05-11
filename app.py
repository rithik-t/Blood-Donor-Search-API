from flask import Flask, request, jsonify
import mysql.connector
from flask_cors import CORS
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
CORS(app)  # Allow frontend to communicate with backend

# Load sensitive information from environment variables
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

# Database connection
db = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_NAME
)
cursor = db.cursor(dictionary=True)

# API to fetch donors based on blood group
@app.route('/search', methods=['GET'])
def search_donors():
    blood_group = request.args.get('bloodGroup')

    if not blood_group:
        return jsonify({"error": "Blood group parameter is missing"}), 400
    
    # Sanitize input to prevent SQL injection
    cursor.execute("SELECT * FROM donors WHERE blood_group = %s", (blood_group,))
    donors = cursor.fetchall()

    return jsonify(donors)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
