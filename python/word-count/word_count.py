import re
def word_count(phrase):
    presence = {}
    for word in re.split("(?:(?:(?!'t))[\W_])", phrase.lower()):
        if len(word) > 0:
            presence[word] = presence.get(word, 0) + 1
    return presence
