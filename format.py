import re


def for_say(data):
    return re.sub(r"\'", "\\'", data)


def for_google_search(data):
    return re.sub(' ', '+', data)


def byteify(input):     # http://stackoverflow.com/questions/956867/how-to-get-string-objects-instead-of-unicode-ones-from-json-in-python
    if isinstance(input, dict):
        return {byteify(key): byteify(value) for key, value in input.iteritems()}
    elif isinstance(input, list):
        return [byteify(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input
