# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime


# Create your models here.



class Brand(models.Model):
    brand_name=models.CharField(max_length=128)
    mft_date=models.CharField(max_length=128)

class Category(models.Model):
    cat_name=models.CharField(max_length=128)
    cat_type=models.CharField(max_length=128)

class Product_table(models.Model):
    product_id = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length=128)
    product_price = models.IntegerField()
    product_color = models.CharField(max_length=128)
    product_cat=models.ForeignKey(Category)
    product_brand=models.ForeignKey(Brand)
