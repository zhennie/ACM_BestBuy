__author__ = 'ash'
from xml.etree import cElementTree
import mysql.connector
import os

def str_to_bool(s):
    if s in ["no","false","False"]:
        return "0"
    else:
        return "1"

def removeNonAscii(s): return "".join(i for i in s if ord(i) < 128)


path = '/home/ash/Documents/ACM/product_data/products'

con = mysql.connector.connect(host='localhost', user='ash', password='5188', database='ACM')
cur = con.cursor()

try:
    cur.execute('DROP TABLE IF EXISTS product_ship')
except Exception, e:
    print e.args[0]
    if e.args[0] == 1064:
        print "Table do not exist, dropping failed "
try:
    cur.execute('DROP TABLE IF EXISTS product_category')
except Exception, e:
    print e.args[0]
    if e.args[0] == 1064:
        print "Table do not exist, dropping failed "
try:
    cur.execute('DROP TABLE IF EXISTS product_freq_purchase')
except Exception, e:
    print e.args[0]
    if e.args[0] == 1064:
        print "Table do not exist, dropping failed "
try:
    cur.execute('DROP TABLE IF EXISTS product')
except Exception, e:
    print e.args[0]
    if e.args[0] == 1064:
        print "Table do not exist, dropping failed "

cur.execute("""
    CREATE TABLE product(sku VARCHAR(50) PRIMARY KEY, productId VARCHAR(50), name VARCHAR(50), source VARCHAR(50),
    type VARCHAR(50), startDate VARCHAR(50), activeUpdateDate VARCHAR(50), regularPrice VARCHAR(50),
    salePrice VARCHAR(50), planPrice VARCHAR(50), priceWithPlan VARCHAR(50), minimumDisplayPrice VARCHAR(50),
    restrictedSalePrice VARCHAR(50), priceUpdateDate VARCHAR(50), salesRankShortTerm VARCHAR(50),
    salesRankMediumTerm VARCHAR(50), salesRankLongTerm VARCHAR(50), bestSellingRank VARCHAR(50),
    customerReviewCount VARCHAR(50), customerReviewAverage VARCHAR(50), inStoreAvailabilityUpdateDate VARCHAR(50),
    itemUpdateDate VARCHAR(50), onlineAvailabilityUpdateDate VARCHAR(50), releaseDate VARCHAR(50),
    shippingCost VARCHAR(50), shortDescription VARCHAR(500), manufacturer VARCHAR(50), originalReleaseDate VARCHAR(50),
    quantityLimit VARCHAR(50), relatedBestBuySkus VARCHAR(50), longDescription VARCHAR(5000), new TINYINT,
    active TINYINT, onSale TINYINT, advertisedPriceRestriction TINYINT, preowned TINYINT, freeShipping TINYINT,
    inStoreAvailability TINYINT, onlineAvailability TINYINT, specialOrder TINYINT, inStorePickup TINYINT,
    friendsAndFamilyPickup TINYINT, homeDelivery TINYINT)
    """
    )

cur.execute('CREATE TABLE product_freq_purchase(sku VARCHAR(50), subsku VARCHAR(50), FOREIGN KEY (sku) '
            'REFERENCES product(sku), FOREIGN KEY (subsku) REFERENCES product(sku))')

cur.execute('CREATE TABLE product_category(sku VARCHAR(50), id VARCHAR(50), name VARCHAR(50), '
            'FOREIGN KEY (sku) REFERENCES product(sku), FOREIGN KEY (id) REFERENCES category(CAT_ID))')

cur.execute('CREATE TABLE product_ship(sku VARCHAR(50), ground VARCHAR(50), secondDay VARCHAR(50), '
            'nextDay VARCHAR(50), vendorDelivery VARCHAR(50), FOREIGN KEY (sku) REFERENCES product(sku))')

for dir_entry in os.listdir(path):
    dir_entry_path = os.path.join(path, dir_entry)
    print dir_entry_path

    fd = open(dir_entry_path, 'r')
    content = fd.read()
    fd.close()
    content = removeNonAscii(content)
    xml_tree = cElementTree.fromstring(content)

    list_of_product = []
    sub_sku = []
    sub_cat = []
    sub_ship = []

    for el in xml_tree.findall('product'):
        sku_str = ''
        productId_str = ''
        name_str = ''
        source_str = ''
        type_str = ''
        startDate_str = ''
        activeUpdateDate_str = ''
        regularPrice_str = ''
        salePrice_str = ''
        planPrice_str = ''
        priceWithPlan_str = ''
        minimumDisplayPrice_str = ''
        restrictedSalePrice_str = ''
        priceUpdateDate_str = ''
        salesRankShortTerm_str = ''
        salesRankMediumTerm_str = ''
        salesRankLongTerm_str = ''
        bestSellingRank_str = ''
        customerReviewCount_str = ''
        customerReviewAverage_str = ''
        inStoreAvailabilityUpdateDate_str = ''
        itemUpdateDate_str = ''
        onlineAvailabilityUpdateDate_str = ''
        releaseDate_str = ''
        shippingCost_str = ''
        shortDescription_str = ''
        manufacturer_str = ''
        originalReleaseDate_str = ''
        quantityLimit_str = ''
        relatedBestBuySkus_str = ''
        longDescription_str = ''
        new_boo = ''
        active_boo = ''
        onSale_boo = ''
        advertisedPriceRestriction_boo = ''
        preowned_boo = ''
        freeShipping_boo = ''
        inStoreAvailability_boo = ''
        onlineAvailability_boo = ''
        specialOrder_boo = ''
        inStorePickup_boo = ''
        friendsAndFamilyPickup_boo = ''
        homeDelivery_boo = ''

        to_add = []

        for ch in el.getchildren():
            if 'sku' == ch.tag:
                sku_str = ch.text

            elif 'productId' == ch.tag:
                productId_str = ch.text

            elif 'name' == ch.tag:
                name_str = ch.text

            elif 'source' == ch.tag:
                source_str = ch.text

            elif 'type' == ch.tag:
                type_str = ch.text

            elif 'startDate' == ch.tag:
                startDate_str = ch.text

            elif 'activeUpdateDate' == ch.tag:
                activeUpdateDate_str = ch.text

            elif 'regularPrice' == ch.tag:
                regularPrice_str = ch.text

            elif 'salePrice' == ch.tag:
                salePrice_str = ch.text

            elif 'planPrice' == ch.tag:
                planPrice_str = ch.text

            elif 'priceWithPlan' == ch.tag:
                priceWithPlan_str = ch.text

            elif 'minimumDisplayPrice' == ch.tag:
                minimumDisplayPrice_str = ch.text

            elif 'restrictedSalePrice' == ch.tag:
                restrictedSalePrice_str = ch.text

            elif 'priceUpdateDate' == ch.tag:
                priceUpdateDate_str = ch.text

            elif 'salesRankShortTerm' == ch.tag:
                salesRankShortTerm_str = ch.text

            elif 'salesRankMediumTerm' == ch.tag:
                salesRankMediumTerm_str = ch.text

            elif 'salesRankLongTerm' == ch.tag:
                salesRankLongTerm_str = ch.text

            elif 'bestSellingRank' == ch.tag:
                bestSellingRank_str = ch.text

            elif 'customerReviewCount' == ch.tag:
                customerReviewCount_str = ch.text

            elif 'customerReviewAverage' == ch.tag:
                customerReviewAverage_str = ch.text

            elif 'inStoreAvailabilityUpdateDate' == ch.tag:
                inStoreAvailabilityUpdateDate_str = ch.text

            elif 'itemUpdateDate' == ch.tag:
                itemUpdateDate_str = ch.text

            elif 'onlineAvailabilityUpdateDate' == ch.tag:
                onlineAvailabilityUpdateDate_str = ch.text

            elif 'releaseDate' == ch.tag:
                releaseDate_str = ch.text

            elif 'shippingCost' == ch.tag:
                shippingCost_str = ch.text

            elif 'shortDescription' == ch.tag:
                shortDescription_str = ch.text

            elif 'manufacturer' == ch.tag:
                manufacturer_str = ch.text

            elif 'originalReleaseDate' == ch.tag:
                originalReleaseDate_str = ch.text

            elif 'quantityLimit' == ch.tag:
                quantityLimit_str = ch.text

            elif 'relatedBestBuySkus' == ch.tag:
                relatedBestBuySkus_str = ch.text

            elif 'longDescription' == ch.tag:
                longDescription_str = ch.text

            elif 'new' == ch.tag:
                new_boo = str_to_bool(bool(ch.text))

            elif 'active' == ch.tag:
                active_boo = str_to_bool(bool(ch.text))

            elif 'onSale' == ch.tag:
                onSale_boo = str_to_bool(bool(ch.text))

            elif 'advertisedPriceRestriction' == ch.tag:
                advertisedPriceRestriction_boo = str_to_bool(bool(ch.text))

            elif 'preowned' == ch.tag:
                preowned_boo = str_to_bool(bool(ch.text))

            elif 'freeShipping' == ch.tag:
                freeShipping_boo = str_to_bool(bool(ch.text))

            elif 'inStoreAvailability' == ch.tag:
                inStoreAvailability_boo = str_to_bool(bool(ch.text))

            elif 'onlineAvailability' == ch.tag:
                onlineAvailability_boo = str_to_bool(bool(ch.text))

            elif 'specialOrder' == ch.tag:
                specialOrder_boo = str_to_bool(bool(ch.text))

            elif 'inStorePickup' == ch.tag:
                inStorePickup_boo = str_to_bool(bool(ch.text))

            elif 'friendsAndFamilyPickup' == ch.tag:
                friendsAndFamilyPickup_boo = str_to_bool(bool(ch.text))


            elif 'homeDelivery' == ch.tag:
                homeDelivery_boo = str_to_bool(bool(ch.text))

            elif 'frequentlyPurchasedWith' == ch.tag:
                if ch.text == None:
                    sub_sku.append([sku_str, ''])
                else:
                    for sub in ch.getchildren():
                        sub_sku.append([sku_str, ch.text])

            elif 'categoryPath' == ch.tag:
                if ch.text == None:
                    sub_cat.append([sku_str, '', ''])
                else:
                    sub_catid = ''
                    sub_catname = ''
                    for cat in ch.getchildren():
                        for sub in cat.getchildren():
                            if sub.tag == 'id':
                                sub_catid = sub.text
                            elif sub.tag == 'name':
                                sub_catname = sub.text
                        sub_cat.append([sku_str, sub_catid, sub_catname])

            elif 'shipping' == ch.tag:
                if ch.text == None:
                    sub_ship.append([sku_str, '', '', '', ''])
                else:
                    ship_ground = ''
                    ship_sec = ''
                    ship_next = ''
                    ship_vendor = ''
                    for ship in ch.getchildren():
                        if ship.tag == 'ground':
                            ship_ground = ship.text
                        elif ship.tag == 'secondDay':
                            ship_sec = ship.text
                        elif ship.tag == 'nextDay':
                            ship_next = ship.text
                        elif ship.tag == 'vendorDelivery':
                            ship_vendor = ship.text
                    sub_ship.append([sku_str, ship_ground, ship_sec, ship_next, ship_vendor])

        to_add = [sku_str, productId_str, name_str, source_str, type_str, startDate_str, activeUpdateDate_str,
                  regularPrice_str, salePrice_str, planPrice_str, priceWithPlan_str, minimumDisplayPrice_str,
                  restrictedSalePrice_str, priceUpdateDate_str, salesRankShortTerm_str, salesRankMediumTerm_str,
                  salesRankLongTerm_str, bestSellingRank_str, customerReviewCount_str, customerReviewAverage_str,
                  inStoreAvailabilityUpdateDate_str, itemUpdateDate_str, onlineAvailabilityUpdateDate_str,
                  releaseDate_str, shippingCost_str, shortDescription_str, manufacturer_str, originalReleaseDate_str,
                  quantityLimit_str, relatedBestBuySkus_str, longDescription_str, new_boo, active_boo, onSale_boo,
                  advertisedPriceRestriction_boo, preowned_boo, freeShipping_boo, inStoreAvailability_boo,
                  onlineAvailability_boo, specialOrder_boo, inStorePickup_boo, friendsAndFamilyPickup_boo,
                  homeDelivery_boo]

        list_of_product.append(to_add)

    for x in list_of_product:
        # print x[0]

        xs = map(lambda s:s or "", x)

        cur.execute(
            # """
            # INSERT INTO product(sku) VALUES(%s)
            # """
            """
            INSERT INTO product(sku, productId, name, source, type, startDate, activeUpdateDate, regularPrice,
            salePrice, planPrice, priceWithPlan, minimumDisplayPrice, restrictedSalePrice, priceUpdateDate,
            salesRankShortTerm, salesRankMediumTerm, salesRankLongTerm, bestSellingRank, customerReviewCount,
            customerReviewAverage, inStoreAvailabilityUpdateDate, itemUpdateDate, onlineAvailabilityUpdateDate,
            releaseDate, shippingCost, shortDescription, manufacturer, originalReleaseDate, quantityLimit,
            relatedBestBuySkus, longDescription, new, active, onSale, advertisedPriceRestriction, preowned,
            freeShipping, inStoreAvailability, onlineAvailability, specialOrder, inStorePickup,
            friendsAndFamilyPickup, homeDelivery) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s,
            %s, %s, %s,
            %s, %s, %s,
            %s, %s, %s)
            """, (x[0:43])
            # """
            # INSERT INTO product(sku, productId, name, source, type, startDate, activeUpdateDate, regularPrice,
            # salePrice, planPrice, priceWithPlan, minimumDisplayPrice, restrictedSalePrice, priceUpdateDate,
            # salesRankShortTerm, salesRankMediumTerm, salesRankLongTerm, bestSellingRank, customerReviewCount,
            # customerReviewAverage, inStoreAvailabilityUpdateDate, itemUpdateDate, onlineAvailabilityUpdateDate,
            # releaseDate, shippingCost, shortDescription, manufacturer, originalReleaseDate, quantityLimit,
            # relatedBestBuySkus, longDescription) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
            # %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            # """, (x[0:31])
        )

    #
    # for x in sub_sku:
    #     cur.execute('INSERT INTO product_freq_purchase(sku, subsku) VALUES(%s, %s)', (x[0], x[1]))

    # for x in sub_cat:
    #     cur.execute('INSERT INTO product_category(sku, id, name) VALUES(%s, %s, %s)', (x[0], x[1], x[2]))
    #
    # for x in sub_ship:
    #     cur.execute('INSERT INTO product_ship(sku, ground, secondDay, nextDay, vendorDelivery) VALUES(%s, %s, %s, %s, %s)', (x[0:5]))

    con.commit()













# dir = os.path.join(path, os.listdir(path)[0])
# table_index = open(dir, 'r')
# table_col = table_index.read()
# table_index.close()
# table_col = removeNonAscii(table_col)
# table_tree = cElementTree.fromstring(table_col)
# list_col = []
#
# print dir

# index_el = table_tree.findall('product')[0]
#
# for ch in index_el:
#     # tag = ch.tag.upper()
#     list_col.append(ch.tag)
#     print ch.text
#
# print list_col



