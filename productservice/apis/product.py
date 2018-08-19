import django

django.setup()
from productservice.db.productApp.models import Product_table as prod, Brand, Category
from flask import jsonify, request
from flask_restful import Resource

django.setup()


def get_product_dict(product):
    return {"Product_id": product.product_id, "Product_name": product.product_name,
            "Product_price": product.product_price,
            "Product_color": product.product_color,
            }


class Products(Resource):
    def get(self, product_id=None):
        if product_id:
            product = prod.objects.get(product_id=product_id)

            product_dict = {"Product_id: ": product.product_id, "product_name": product.product_name,
                            "product_price": product.product_price, "product_color": product.product_color}
            return jsonify({"Product": product_dict})

        product = prod.objects.all()
        product_list = [get_product_dict(x) for x in product]
        return jsonify({"Products": product_list})

    def post(self):
        data = request.get_json(force=True)
        brand_obj = Brand.objects.get(brand_name=data["brandname"])
        cate_obj = Category.objects.get(cat_name=data["catname"])
        print brand_obj, cate_obj
        product_add = prod.objects.create(product_id=data['productid'], product_name=data['productname'],
                                          product_price=data['productprice'], product_color=data['productcolor'],
                                          product_brand=brand_obj,
                                          product_cat=cate_obj)

        product_dict = get_product_dict(product_add)
        return jsonify({"Product": product_dict})

    def put(self, product_id=None):
        data = request.get_json()
        if product_id:
            product = prod.objects.get(product_id=product_id)
            product.product_name = data['newname']
            Brand.brand_name = data['newbrand']
            product.save()
            product_dict = get_product_dict(product)

            return jsonify({"Product: ": product_dict})

    def delete(self):
        data = request.get_json()
        product = prod.objects.filter(product_id=data['productid']).delete()

        product_dict = {"product ": data['productid']}
        return jsonify({"Product: ": product_dict})
