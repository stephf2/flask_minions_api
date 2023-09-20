from flask import jsonify, request
from werkzeug import exceptions
from application import app
from .controllers import index, create, show, update, destroy

@app.route("/minions", methods=["GET", "POST"])
def handle_minions():
    if request.method == "POST": return create()
    elif request.method == "GET": return index()
    else: "Method not allowed", 405
    
@app.route("/minions/<id_or_name>", methods=["GET", "PATCH", "DELETE"])
def show_minion(id_or_name):
    if request.method == "GET": return show(id_or_name)
    elif request.method == "PATCH": return update(id_or_name)
    elif request.method == "DELETE": return destroy(id_or_name)
    else: "Method not allowed", 405
    
@app.errorhandler(exceptions.NotFound)
def handle_404(err):
    return jsonify({"error": f'Error! {err}'}), 404

@app.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return jsonify({"error": f'Error! {err}'}), 500

@app.errorhandler(exceptions.BadRequest)
def handle_400(err):
    return jsonify({"error": f'Error! {err}'}), 400
