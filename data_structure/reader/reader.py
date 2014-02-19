from xml.etree import cElementTree
from data_structure.category import Category

__author__ = 'ash'

def removeNonAscii(s): return "".join(i for i in s if ord(i)<128)


class Reader:

    def __init__(self, path, db_con):
        self.path = path
        self.db_con = db_con
        self.data = []

    def read(self):
        pass

    def export_to_database(self, table):
        pass


class CategoryReader(Reader):

    def __init__(self, path, db_con):
        """

        @param path: Where the file is locate
        @param db_con: A DB connection we can use.
        """
        Reader.__init__(self, path, db_con)

    def read(self):
        """
        read list of Category from path.
        @return: list of data
        """
        fd = open(self.path, "r")
        content = fd.read()
        fd.close()
        content = removeNonAscii(content)
        xml_tree = cElementTree.fromstring(content)

        list_of_data = []

        for el in xml_tree.findall('category'):
            id_str = ""
            name_str = ""

            for ch in el.getchildren():

                if 'id' == ch.tag:
                    id_str = removeNonAscii(ch.text)

                if 'name' == ch.tag:
                    name_str = removeNonAscii(ch.text)

            to_add = Category(id_str, name_str)
            list_of_data.append(to_add)

        self.data = list_of_data
        return self.data

    def export_to_database(self, table, print_freq=100):
        if len(self.data) == 0:
            self.read()
        try:
            self.db_con.exec_query('DROP TABLE IF EXISTS %s' % table)
        except Exception, e:
            print e.args[0]
            if e.args[0] == 1064:
                print "Table do not exist, dropping failed "

        self.db_con.exec_query('CREATE TABLE %s(CAT_ID VARCHAR(50) PRIMARY KEY, Cat_Name VARCHAR(50))' % table)

        count = 0
        for d in self.data:
            count += 1
            format_str, key_set = d.to_import_args(table)
            self.db_con.exec_query(format_str, key_set)
            if count % print_freq == 0:
                print "Inserted %d Row into database" % count
        self.close()

    def close(self):
        self.db_con.close()