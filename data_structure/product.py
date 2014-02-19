#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'ash'


class Product(object):
    def __init__(self, sku, categories_id, categories_name, product_name):
        self.sku = sku
        self.categories_id = categories_id
        self.categories_name = categories_name
        self.product_name = product_name
