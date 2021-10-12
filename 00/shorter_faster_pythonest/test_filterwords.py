from filterwords import filterwords


def test_one_letter():
    assert filterwords('a', 0) == ['a']


def test_one_letter_with_lenght_1():
    assert filterwords('a', 1) == []


def test_two_letter_with_lenght_0():
    assert filterwords("ga", 0) == ["ga"]


def test_one_word_with_exclamation():
    assert filterwords("42sp!", 0) == ["42sp"]


def test_one_word_with_coma():
    assert filterwords("42sp,", 0) == ["42sp"]


def test_one_word_with_point():
    assert filterwords("42sp.", 0) == ["42sp"]


def test_two_words_with_lenght_4():
    assert filterwords("gabriel vito", 4) == ["gabriel"]


def test_four_words_with_three_puntuation_lenght_5():
    assert filterwords(
            "gabriel! vitor, sales?, machado.", 5) == ["gabriel", "machado"]


def test_passing_one_number_as_first_parameter():
    assert filterwords(300, 3) == "ERROR"


def test_one_big_string():
    assert filterwords("""A robot must protect its own existence\
 as long as such protection\
 does not conflict with the First or Second Law
""", 6) == ['protect', 'existence', 'protection', 'conflict']
