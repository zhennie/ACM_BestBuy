#!/usr/bin/python
# -*- coding: utf-8 -*-
from data_structure.reader.reader import CategoryReader
from database_util.database_connection import DatabaseConnection


if __name__ == "__main__":
    path = '/home/ash/Documents/ACM/product_data/categories/categories_0001_abcat0010000_to_pcmcat99300050000.xml'
    reader = CategoryReader(path, DatabaseConnection())
    reader.export_to_database("category", print_freq=1000)