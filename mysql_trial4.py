#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'ash'

#this trial4 is for Dictionary Cursor example from zetcode

import MySQLdb as mdb

con = mdb.connect('localhost', 'ash', '5188', 'bestbuy')

with con:

    cur = con.cursor(mdb.cursors.DictCursor)
    cur.execute('SELECT * From Writers LIMIT 2')

    rows = cur.fetchall()

    for row in rows:
        print row['ID'], row['Name'], row['AGE']
