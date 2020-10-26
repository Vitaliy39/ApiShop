from db import db

class CourierModel(db.Model):
    __tablename__ = 'couriers'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    zone_id = db.Column(db.Integer, db.ForeignKey('zones.id'))
    zone = db.relationship('ZoneModel')

    def __init__(self, zone_id):
        self.zone_id = zone_id

    def json(self):
        return {'zone_id': self.zone_id}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

