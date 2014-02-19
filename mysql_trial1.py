#!/usr/bin/python
# -*- coding: utf-8 -*-

##the first line above is used to tell the computer to run the program with python if not otherwise specified
##the second line above the second line above is used to avoid unicode problem in python which asks python to/
# use unicode to encode instead of default ascii which can only represent 128 characters
__author__ = 'ash'
#example 1 from zetcode.com to show the database version (mysql server)

import MySQLdb as mdb
import sys

try:
    con = mdb.connect('localhost','ash','5188','bestbuy');

    cur = con.cursor()
    cur.execute('SELECT VERSION()')
    ver = cur.fetchone()
    print 'Database version : %s' %ver

except mdb.Error, e:

    print 'Error %d: %s' %(e.args[0], e.args[1])
    sys.exit(1)

finally:
    if con:
        con.close()

__author__ = 'ash'
try:
    # 9/0
    9+"lll"
    9/0
except ZeroDivisionError,e:
    print 'error occurred'
except TypeError,e:
    print 'value error'


print 'haha'
