#!/usr/bin/python
#-*- coding : utf-8 -*-

__author__ = 'ash'
import MySQLdb as mdb

con = mdb.connect('localhost', 'ash', '5188', 'bestbuy')

with con:

    cur = con.cursor()

    cur.execute('UPDATE Writers SET Name = %s WHERE ID = %s', ('Ashton','3'))

    print cur.rowcount

#rowcount counts how many rows been touched by a query

