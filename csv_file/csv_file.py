'''read csv and convert it to ordered dictionary'''
from collections import OrderedDict
import pandas as pd

class CSVFile:
    '''class for csv manipulation'''
    @classmethod
    def to_dictionary_list(cls, filename):
        '''Read CSV File'''
        csv_rows = []
        try:
            data_frame = pd.read_csv(filename, keep_default_na=False)
            records = data_frame.to_dict('records', into=OrderedDict)
            for row in records:
                csv_rows.append(row)
            return csv_rows
        except IOError:
            return False
