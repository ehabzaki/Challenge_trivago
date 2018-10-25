import unittest


from collections import OrderedDict
from validators import validators as v
from converter import converter as c
from csv_file import csv_file as cf

validator = v.Validator()
csv_file = cf.CSV_File()
convert_to = c.Convert_To()
#list_of_dic = csv_file.to_dictionary_list(FILE_CSV)
class TestHotel(unittest.TestCase):


    def setUp(self):
        pass

    def test_validate_url(self):
        self.assertEqual(validator.validateURL("www.google.com"), False)

    def test_stars_validator(self):
        self.assertEqual(validator.validateHotelStars(-1), False)

if __name__ == '__main__':
    unittest.main()
