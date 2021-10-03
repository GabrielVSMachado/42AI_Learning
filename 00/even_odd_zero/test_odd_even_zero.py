from whois import the_odd_even_or_zero
EVEN = "I\'m Even."
ODD = "I\'m Odd."
ZERO = "I\'m Zero."
ERROR = "ERROR"


def test_twelve_is_even():
    assert the_odd_even_or_zero(12) == EVEN


def test_eleven_is_odd():
    assert the_odd_even_or_zero(11) == ODD


def test_zero_is_zero():
    assert the_odd_even_or_zero(0) == ZERO


def test_string_is_ERROR():
    assert the_odd_even_or_zero("gabriel") == ERROR


def test_nine_is_odd():
    assert the_odd_even_or_zero(9) == ODD


def test_ten_is_even():
    assert the_odd_even_or_zero(10) == EVEN


def test_none():
    assert the_odd_even_or_zero() is None


def test_two_args_which_both_number():
    assert the_odd_even_or_zero(12, 3) == ERROR


def test_two_args_with_the_second_None():
    assert the_odd_even_or_zero(3, None) == "ERROR"


def test_two_args_with_the_first_None():
    assert the_odd_even_or_zero(None, 3) == "ERROR"


def test_three_args():
    assert the_odd_even_or_zero(1, 2, 3) == "ERROR"
