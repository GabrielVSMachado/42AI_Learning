from count import text_analyzer


def string_result(number_characters, up_letter, low_letter,
                  punctuation, spaces):
    return """The text contains {} characters:\n
- {} upper letters\n
- {} lower letters\n
- {} punctuation marks\n
- {} spaces""".format(number_characters, up_letter, low_letter,
                      punctuation, spaces)


def test_one_character_lower_case():
    assert text_analyzer('a') == string_result(1, 0, 1, 0, 0)
