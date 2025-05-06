from flask import jsonify

def health_check():
    return jsonify({"message": "success"}), 200