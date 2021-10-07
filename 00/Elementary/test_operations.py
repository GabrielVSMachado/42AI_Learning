from operations import operations


def string_result(Sum, Diff, Product, Quotient, Remainder):
    return f"""
Sum:        {Sum}
Difference: {Diff}
Product:    {Product}
Quotient:   {Quotient}
Remainder:  {Remainder}"""


def test_10_and_3():
    assert operations(10, 3) == string_result(13, 7, 30, 10 / 3, 1)


def test_3_and_10():
    assert operations(3, 10) == string_result(13, -7, 30, 3 / 10, 3)


def test_1_and_0():
    assert operations(1, 0) == """
Sum:        1
Difference: 1
Product:    0
Quotient:   ERROR (div by zero)
Remainder:  ERROR (modulo by zero)"""


def test_None_args():
    assert operations() == operations.__doc__


def test_three_args():
    assert operations(1, 2, 3) == "InputError: too many arguments\n%s" % (operations.__doc__)


def test_strings_as_arguments():
    assert operations("one", "two") == "InputError: only numbers\n{}".format(
                                     operations.__doc__)

def test_strings_with_numbers():
    assert operations("512", "51.2") == f"InputError: only numbers\n{operations.__doc__}"


def test_34223_and_2222():
    assert operations(34223, 2222) == string_result(36445, 32001, 76043506, 34223 / 2222, 34223 % 2222)
