from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Client(db.Model):
    __tablename__ = 'clients'

    #Fields
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    money = db.Column(db.Integer)
    
    #Initialize database
    def __init__(self, name, money):
        self.name = name
        self.money = money
        

    def __repr__(self):
        return '<id {}>'.format(self.id)

    #For JSON serialization purposes
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'money': self.money,
        }
