import application 
class Client(application.db.Model):
    __tablename__ = 'clients'

    #Fields
    id = application.db.Column(application.db.Integer, primary_key=True)
    name = application.db.Column(application.db.String())
    money = application.db.Column(application.db.Integer)

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
            'money': self.money
        }
