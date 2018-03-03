import re
def is_pangram(sentence):
    clean_sentence = re.compile('[^A-Za-z]').sub('', sentence).lower()
    return len(set(clean_sentence)) == 26
