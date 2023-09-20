from flask import jsonify, request
from werkzeug import exceptions
from application import db
from .models import Minion

def index():
    try:
        minions = Minion.query.all()
        data = [m.json for m in minions]
        return jsonify({"minions": data})
    except:
        raise exceptions.InternalServerError("working on it")

def create():
    try:
        name, appearance = request.json.values()
        new_minion = Minion(name, appearance)
        
        db.session.add(new_minion)
        db.session.commit()
        
        return jsonify({"data": new_minion.json}), 201
    except:
        raise exceptions.BadRequest("We cannot process your request.")

def show(id_or_name):
    try: 
        if id_or_name.isdigit():
            minion = Minion.query.filter_by(id=int(id_or_name)).first()
        else:
            minion = Minion.query.filter_by(name=id_or_name).first()

        return jsonify({"data": minion.json}), 200
    except: 
        raise exceptions.NotFound("Minion not found")

def update(id_or_name):
    try:
        data = request.json

        if id_or_name.isdigit():
            minion = Minion.query.filter_by(id=int(id_or_name)).first()
        else:
            minion = Minion.query.filter_by(name=id_or_name).first()
        
        for (attribute, value) in data.items():
            if hasattr(minion, attribute):
                setattr(minion, attribute, value)
        
        db.session.commit()
        
        return jsonify({"data": minion.json})
    except:
        raise exceptions.NotFound("Not found")
    
def destroy(id_or_name):
    try:      
        if id_or_name.isdigit():
            minion = Minion.query.filter_by(id=int(id_or_name)).first()
        else:
            minion = Minion.query.filter_by(name=id_or_name).first()
            
        db.session.delete(minion)
        db.session.commit()
        return f"Minion deleted", 204
    except:
        raise exceptions.NotFound("Could not delete")

