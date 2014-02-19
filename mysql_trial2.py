#!/usr/bin/python
# -*- coding: utf-8 -*-

#example 2 from zetcode to create table and insert contents in database via python

__author__ = 'ash'
import MySQLdb as mdb

con = mdb.connect('localhost','ash','5188','bestbuy');

with con:
#better not use with keyword which is supposed to be similar with try/finally block as I'm not so sure what exactly is it doing

    cur = con.cursor()
    cur.execute('DROP TABLE IF EXISTS Writers')
    cur.execute('CREATE TABLE Writers(ID INT PRIMARY KEY AUTO_INCREMENT, Name VARCHAR(25), AGE INT)')
    cur.execute("INSERT INTO Writers(Name) VALUES('Jack')")
    cur.execute("INSERT INTO Writers(Name, AGE) VALUES('B',88)")
    cur.execute("INSERT INTO Writers(Name) VALUES('C')")
    cur.execute("INSERT INTO Writers(Name, AGE) VALUES('D',150)")

