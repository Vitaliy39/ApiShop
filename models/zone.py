from db import db


class ZoneModel(db.Model):
    __tablename__ = 'zones'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    lang = db.Column(db.Float(10))
    long = db.Column(db.Float(10))
    radius = db.Column(db.Float(10))

    def __init__(self, lat, long, radius):
        self.lat = lat
        self.long = long
        self.radius = radius

    def json(self):
        return {'latitude': self.lat, 'longitude': self.long, 'radius' : self.radius}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
