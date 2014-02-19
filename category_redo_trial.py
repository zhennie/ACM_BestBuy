import sys

__author__ = 'ash'
from xml.etree import cElementTree
import mysql.connector

def removeNonAscii(s): return "".join(i for i in s if ord(i)<128)

fd = open('/home/ash/Documents/ACM/product_data/categories/categories_0001_abcat0010000_to_pcmcat99300050000.xml','r')
content = fd.read()
fd.close()

content = removeNonAscii(content)
xml_tree = cElementTree.fromstring(content)

list_of_data = []
list_of_sub = []
sub_info = []

for el in xml_tree.findall('category'):
    id_str = ''
    name_str = ''

    sub_id = ''
    sub_name = ''

    for ch in el.getchildren():

        if 'id' == ch.tag:
            id_str = removeNonAscii(ch.text)

        if 'name' == ch.tag:
            name_str = removeNonAscii(ch.text)

        if 'subCategories' == ch.tag:

            for sub in ch.getchildren():

                for sub_child in sub.getchildren():
                    sub_add = []

                    if 'id' == sub_child.tag:
                        sub_id = removeNonAscii(sub_child.text)
                        # print sub_id

                    # if 'name' == sub_child.tag:
                    #     sub_name = removeNonAscii(sub_child.text)
                    #     # print sub_name

                    # if sub_id != '' and sub_name != '':

                        sub_add = [id_str, sub_id]
                        sub_info.append(sub_add)
                        # print sub_add


    to_add = [id_str, name_str]
    list_of_data.append(to_add)

con = mysql.connector.connect(host='localhost', user='ash', password='5188', database='ACM')
cur = con.cursor()


try:
    cur.execute('DROP TABLE IF EXISTS subcat')
except Exception, e:
    print e.args[0]
    if e.args[0] == 1064:
        print "Table do not exist, dropping failed "
try:
    cur.execute('DROP TABLE If EXISTS category')
except Exception, e:
    print e.args[0]
    if e.args[0] == 1064:
        print "Table do not exist, dropping failed "


    # print e.args[0]
    # if e.args[0] == 1064:
    #     print "Table do not exist, dropping failed "

cur.execute('CREATE TABLE category(CAT_ID VARCHAR(50) PRIMARY KEY, CAT_NAME VARCHAR(50))')
cur.execute('CREATE TABLE subcat(CAT_ID VARCHAR(50), SUB_ID VARCHAR(50), FOREIGN KEY (CAT_ID) REFERENCES category(CAT_ID),FOREIGN KEY (SUB_ID) REFERENCES category(CAT_ID))')


for x in list_of_data:
    cur.execute('INSERT INTO category (CAT_ID,CAT_NAME) VALUES(%s, %s)', (x[0], x[1]))

con.commit()


for x in sub_info:
    cur.execute('INSERT INTO subcat (CAT_ID, SUB_ID) VALUES(%s, %s)', (x[0], x[1]))

con.commit()

con.close()