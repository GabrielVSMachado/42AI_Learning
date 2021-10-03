from rev_alpha import rev_alpha


def test_1():
    assert rev_alpha("gabriel") == "GABRIEL"[::-1]


def test_2():
    assert rev_alpha("vitor") == "VITOR"[::-1]


def test_3():
    assert rev_alpha("vitor", "machado") == "VITOR MACHADO"[::-1]


def test_4():
    assert rev_alpha("  gabriel  sales \n") == "  GABRIEL  SALES \n"[::-1]
