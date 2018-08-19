from flask import *
from flask_restful import *
from productservice.apis.product import Products

import django
django.setup()
app = Flask(__name__)

api = Api(app, prefix='/productservice/')
api.add_resource(Products,'product/','product/<product_id>')


if __name__ == '__main__':
    app.run(host='localhost',port=2010,debug=True)