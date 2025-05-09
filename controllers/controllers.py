from flask import jsonify,request
from werkzeug.security import generate_password_hash, check_password_hash
from Models.models import *
import hashlib, psycopg2

DB_CONFIG = {
    "dbname": "weather_fetcher_app",
    "user": "postgres",
    "password": "PostRaghu@1",
    "host": "127.0.0.1",
    "port": "5432"
}
create_user_sql = '''Insert into users(id,username, email, password) values (%s,%s, %s, %s)'''

def health_check():
    return jsonify({"message": "success"}), 200

def sign_up():
    data = request.get_json()
    userName = data.get('userName')
    email = data.get('email')
    pw = data.get('password')
    password = hashlib.sha256(pw.encode()).hexdigest()       
    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()      
    new_user = signup(
        username = userName,
        email = email,
        password = password
    )
    cursor.execute(create_user_sql, (new_user.id, new_user.username, new_user.email, new_user.password))
    conn.commit()     
    return jsonify({"user created successfully with id :" : new_user.id}), 200