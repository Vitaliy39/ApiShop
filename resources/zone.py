from flask_restful import Resource, reqparse
from models.zone import ZoneModel
from flasgger import Swagger, swag_from


class Zone(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('lat',
                        type=float,
                        required=True)
    parser.add_argument('long',
                        type=float,
                        required=True)
    parser.add_argument('radius',
                        type=float,
                        required=True)

#@swag_from('docs/zone_spec.yml')
    def post(self):
        """
        Create a new zone for courier service
        ---
        tags:
          - zones
        parameters:
          - in: body
            name: body
            schema:
              id: Zone
              required:
                - lat
                - long
                - radius
              properties:
                lat:
                  type: number
                  description: latitude
                long:
                  type: number
                  description: longitude
                radius:
                   type: number
                   description: radius
        responses:
          200:
            description: new zone created
            parameters:
             name:answer
            schema:
              properties:
                message:
                  type: string
                  description: The answer
                """
        data = Zone.parser.parse_args()
        zone = ZoneModel(**data)
        print(data)
        #return jso


