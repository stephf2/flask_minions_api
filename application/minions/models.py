from application import db, app

app.app_context().push()

class Minion(db.Model):
    __tablename__ = "minions"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    appearance = db.Column(db.String(100), nullable=False)
    
    def __init__(self, name, appearance):
        self.name = name
        self.appearance = appearance

    def __repr__(self):
        return f"Minion(id: {self.id}, name: {self.name})"
    
    @property
    def json(self):
        return {"id": self.id, "name": self.name, "appearance": self.appearance}
