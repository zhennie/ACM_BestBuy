#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'ash'

#this trial3 is for example of Retrieving Data from zetcode

import MySQLdb as mdb

con = mdb.connect('localhost', 'ash', '5188', 'bestbuy');

with con:
#better not use 'with' keyword which is supposed to be similar with try/finally block as I'm not so sure what exactly is it doing

    cur = con.cursor()
    cur.execute('SELECT * FROM Writers')

    rows = cur.fetchall()

    for row in rows:
        print row

#fetchall method read all rows of a table to cursor at a time, we may also read rows one by one with fetchone method
    cur.execute('SELECT * FROM Writers')

    for i in range(cur.rowcount):
        row = cur.fetchone()
        print row[0], row[1], row[2]



