import re


def for_say(data):
    return re.sub(r"\'", "\\'", data)


def for_google_search(data):
    return re.sub(' ', '+', data)
