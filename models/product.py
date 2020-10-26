from db import db
from models.courier import CourierModel
from myFuncs import distance


class ProductModel(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    lat = db.Column(db.Float(10))
    long = db.Column(db.Float(10))
    #zone_id = db.Column(db.Integer, db.Fo('couriers.zone_id'))
    courier_id = db.Column(db.Integer, db.ForeignKey('couriers.id'))
    courier = db.relationship('CourierModel')

    def __init__(self, lat, long, zone_id, courier_id):
        self.lat = lat
        self.long = long
        self.zone_id = zone_id
        self.courier_id = courier_id


    def json(self):
        return {'latitute': self.lat,
                'longitude': self.long,
                'zone_id' : self.zone_id,
                'courier_id': self.courier_id }



