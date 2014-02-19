from data_structure.category import Category

__author__ = 'ash'
from bs4 import BeautifulSoup
from bs4 import BeautifulStoneSoup

import xml.etree.cElementTree as ET

def removeNonAscii(s): return "".join(i for i in s if ord(i)<128)

# this is a comment
path = '/home/ash/Documents/ACM/product_data/categories/categories_0001_abcat0010000_to_pcmcat99300050000.xml'
xml_file = open(path, 'r')
content = xml_file.read()
xml_file.close()

content = removeNonAscii(content)

soup = BeautifulSoup(content)
data = soup.find_all('category', {})

root = soup.find("categories")

for x in root.children:
    id = x.find("id")
    name = x.find("name")
    path = []

    for p in x.find("path"):
        sub_id = x.find("id")
        sub_name = x.find("name")
        path_cat = Category(sub_id,sub_name)
        path.append(path_cat)

    subCat = []
    for p in x.find("subCategories"):
        sub_id = x.find("id")
        sub_name = x.find("name")
        path_cat = Category(sub_id,sub_name)
        path.append(path_cat)

