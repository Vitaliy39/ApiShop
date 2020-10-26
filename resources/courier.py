from flask_restful import Resource, reqparse
from models.courier import CourierModel

class Courier(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('zone_id',
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
      - Couriers
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
        data = Courier.parser.parse_args()
        zone = CourierModel(**data)
        print(data)
        try:
            zone.save_to_db()
        except:
            return {'message': 'An error'}, 500

