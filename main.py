#!/usr/bin/env python
'''main file'''
from validators import validators as v
from converter import converter as c
from csv_file import csv_file as cf

def main():
    '''main function'''
    file_csv = './data/hotels.csv'
    file_json = './data/hotels.json'
    file_html = './data/hotels.html'
    validator = v.Validator()
    csv_file = cf.CSVFile()
    convert_to = c.Converter()
    list_of_hotels = csv_file.to_dictionary_list(file_csv)
    clean_hotels_list = []
    if list_of_hotels is not False:
        for hotel in list_of_hotels:
            count = 0
            for key in hotel:
                if  hotel[key] == "":
                    count = count + 1
            if count != len(hotel):
                if validator.validate_hotel_stars(hotel["stars"]) and validator.validate_url(hotel["uri"]):
                    clean_hotels_list.append(hotel)
        json_file_created = convert_to.json_file(clean_hotels_list, file_json)
        html_file_created = convert_to.html_file(clean_hotels_list, file_html)
        if json_file_created is True:
            print("JSON file is created")
        else:
            print("Faild to create JSON file")
        if html_file_created is True:
            print("HTML file is created")
        else:
            print("Faild to create HTML file")
    else:
        print('Faild to read csv file')
if __name__ == "__main__":
    main()
