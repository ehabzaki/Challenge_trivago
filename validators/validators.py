'''validate url,hotel stars'''
try:
    # python2
    from urlparse import urlparse
except ImportError:
    # python3
    from urllib.parse import urlparse

class Validator:
    '''validators:url,hotels stars'''
    @classmethod
    def validate_url(cls, url):
        '''check valid url'''
        try:
            result = urlparse(url)
            return all([result.scheme, result.netloc, result.path])
        except ValueError:
            return False
    @classmethod
    def validate_hotel_stars(cls, numbers):
        '''validate number of stars not less than 0 and not greater than 5'''
        string_to_int = int(numbers)
        if 0 <= string_to_int <= 5:
            return True
        return False
