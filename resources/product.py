from flask_restful import Resource, reqparse
from models.courier import CourierModel
from models.zone import ZoneModel
from myFuncs import distance

class Product(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('lat',
                        type=float,
                        required=True)
    parser.add_argument('long',
                        type=float,
                        required=True)

    def post(self):
        """
    First line is the summary
    All following lines until the hyphens is added to description
    the format of the first lines until 3 hyphens will be not yaml compliant
    but everything below the 3 hyphens should be.
    ---
    tags:
      - Products
    parameters:
      - in: path
        name: username
        type: string
    responses:
      200:
        description: A single user item
        schema:
          id: rec_username
          properties:
            username:
              type: string
              description: The name of the user
              default: 'steve-harris'
        :return:
        """
        data = Product.parser.parse_args()
        cour = CourierModel.query.all()
        zones = ZoneModel.query.all()
        min = 6400
        for i in cour:
            for zone in zones:
                if i.zone_id == zone.id:
                    s = distance((data['lat'], data['long']), (zone.lat, zone.long))
                    if min > s and s <= zone.radius:
                        min = s
                        zone_min = i.zone_id
                        courier_min = i.id
        return{'zone_id': zone_min, 'courier_id': courier_min}
#

