from flask import Flask, request, jsonify
import mysql.connector
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow frontend to communicate with backend

# Database connection
db = mysql.connector.connect(
    host=#"enter the host",
    user=#"enter the user",
    password=#"enter the password",  # Add your MySQL password if needed
    database=#"enter the database name"
)
cursor = db.cursor(dictionary=True)

# API to fetch donors based on blood group
@app.route('/search', methods=['GET'])
def search_donors():
    blood_group = request.args.get('bloodGroup')
    if not blood_group:
        return jsonify({"error": "Blood group parameter is missing"}), 400
    
    cursor.execute("SELECT * FROM donors WHERE blood_group = %s", (blood_group,))
    donors = cursor.fetchall()
    
    return jsonify(donors)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
