#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'ash'


class Category(object):
    def __init__(self, category_id, category_name):
        self.category_id = category_id
        self.category_name = category_name

    def __str__(self):
        return "Category["+self.category_id +" : "+ self.category_name + "]"

    def __repr__(self):
        return self.__str__()

    def to_import_args(self,table_name):
        format_query_str = "INSERT INTO " + table_name +"(CAT_ID,Cat_Name) VALUES(%s,%s)"
        query_tuple = (self.category_id, self.category_name)
        return format_query_str,query_tuple
