#!/usr/bin/python
# -*- coding : utf-8 -*-
__author__ = 'ash'

import MySQLdb as mdb

con = mdb.connect('localhost', 'ash', '5188', 'bestbuy')

with con:

    cur = con.cursor()
    cur.execute('SELECT * FROM Writers')

    rows = cur.fetchall()

    desc = cur.description

    print desc

    for row in rows:
        print row
