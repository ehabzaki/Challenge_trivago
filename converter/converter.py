'''convert dictionary or OrderedDictionary to html,json..'''
import codecs
import json
import pandas 
class Converter:
    '''this class convert dic to json or html file'''
    @classmethod
    def html_file(cls, csv_rows, html_file):
        '''convert list of dictionary to html'''
        try:
            data_frame = pandas.DataFrame(csv_rows)
            pandas.set_option('display.max_colwidth', -1)
            data_frame.to_html(html_file)
            line = '<head><meta charset="UTF-8"></head>'
            with open(html_file, 'r+') as file_html:
                try:
                    content = file_html.read()
                    file_html.seek(0, 0)
                    file_html.write(line.rstrip('\r\n') + '\n' + content)
                    return True
                except IOError:
                    return False
        except TypeError:
            return False

    @classmethod
    def json_file(cls, csv_rows, json_file):
        '''convert list of dictionary to json'''
        try:
            json_format = json.dumps(csv_rows, sort_keys=False, indent=4, separators=(',', ': '), ensure_ascii=False)
            with codecs.open(json_file, 'w', encoding='utf-8') as file_json:
                try:
                    file_json.write(json_format)
                    return True
                except IOError:
                    return False
        except TypeError:
            return False
