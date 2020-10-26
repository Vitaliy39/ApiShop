from flask import Flask
from flask_restful import Api
from flasgger import Swagger, swag_from
from resources.zone import Zone
from resources.courier import Courier
from resources.product import Product


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['SWAGGER'] = {
    'title': 'Small RESTful'
}
swag = Swagger(app)
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

api.add_resource(Zone, '/zone/')
api.add_resource(Courier, '/courier/')
api.add_resource(Product, '/product/')

if __name__=='__main__':
    from db import db
    db.init_app(app)
    print(app.url_map)
    app.run(port=5000, debug=True)
