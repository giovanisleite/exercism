import re
def is_isogram(string):
    clean_string = re.compile('[^a-zA-Z]').sub('', string).lower()
    return len(set(clean_string)) == len(clean_string)
