from flask import jsonify, request
from werkzeug import exceptions
from application import app, db

@app.route("/")
def bello():
    return jsonify({
        "message": "Bello, welcome",
        "description": "Minions API",
        "endpoints": [
            "GET /"
        ]
    }), 200
