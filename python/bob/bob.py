import re


def hey(phrase):
    if len(re.compile('\s').sub('', phrase)) == 0:
        return 'Fine. Be that way!'
    if is_a_scream(phrase) and is_a_question(phrase):
        return "Calm down, I know what I'm doing!"
    if is_a_question(phrase):
        return 'Sure.'
    if is_a_scream(phrase):
        return 'Whoa, chill out!'
    return 'Whatever.'


def is_a_question(phrase):
    return phrase.strip()[-1] == '?'


def is_a_scream(phrase):
    capitalized_letters = [(letter.isupper()) for letter in phrase if letter.isalpha()]
    return len(capitalized_letters) > 0 and all(capitalized_letters)
