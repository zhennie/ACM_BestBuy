__author__ = 'ash'
from xml.etree import cElementTree
import mysql.connector

import os

def removeNonAscii(s):
    if s is None:
        return ""
    return "".join(i for i in s if ord(i)<128)

path = '/home/ash/Documents/ACM/product_data/reviews'

con = mysql.connector.connect(host='localhost', user='ash', password='5188', database='ACM')
cur = con.cursor()

try:
    cur.execute('DROP TABLE IF EXISTS review')
except Exception, e:
    print e.args[0]
    if e.args[0] == 1064:
        print "Table do not exist, dropping failed "

cur.execute('CREATE TABLE review(REVIEW_ID'
            ' VARCHAR(50) PRIMARY KEY, SKU VARCHAR(50), '
            'REVIEWER VARCHAR(50), ABOUTME VARCHAR(50), '
            'RATING FLOAT, TITLE VARCHAR(50), '
            'COMMENT VARCHAR(5000), SUBTIME VARCHAR(50))')


for dir_entry in os.listdir(path):
    dir_entry_path = os.path.join(path, dir_entry)
    print dir_entry_path

    fd = open(dir_entry_path, 'r')
    content = fd.read()
    fd.close()

    content = removeNonAscii(content)
    xml_tree = cElementTree.fromstring(content)

    list_of_data = []

    for el in xml_tree.findall('review'):
        id_str = ''
        sku_str = ''
        reviewer_str = ''
        about_me_str = ''
        rating_str = ''
        title_str = ''
        comment_str = ''
        sub_time_str = ''

        for ch in el.getchildren():

            if 'id' == ch.tag:
                id_str = removeNonAscii(ch.text)

            elif 'sku' == ch.tag:
                sku_str = removeNonAscii(ch.text)

            elif 'reviewer' == ch.tag:
                name = ch.getchildren()
                reviewer_str = removeNonAscii(name[0].text)

            elif 'aboutMe' == ch.tag:
                about_me_str = removeNonAscii(ch.text)

            elif 'rating' == ch.tag:
                rating_str = removeNonAscii(ch.text)

            elif 'title' == ch.tag:
                title_str = removeNonAscii(ch.text)

            if 'comment' == ch.tag:
                comment_str = removeNonAscii(ch.text)

            if 'submissionTime' == ch.tag:
                sub_time_str = removeNonAscii(ch.text)

        to_add = [id_str, sku_str, reviewer_str, about_me_str, rating_str, title_str, comment_str, sub_time_str]

        list_of_data.append(to_add)


    for x in list_of_data:
        print "----------------------"
        for i in x:
            print i

        print "+++++++++++++++++++++++"
        cur.execute('INSERT INTO review (REVIEW_ID, SKU, REVIEWER, ABOUTME, RATING, TITLE, COMMENT, SUBTIME) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)',(x[0:8]))



con.commit()
con.close()





