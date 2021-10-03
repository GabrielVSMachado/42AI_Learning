# revert a string and if more then one is given join all in one string and revert
def rev_alpha(*strings):
    lst_normal_order = [i[::-1].swapcase() for i in strings[::-1]]
    if len(strings) == 1:
        lst_reversed_order = "".join(lst_normal_order)
    else:
        lst_reversed_order = " ".join(lst_normal_order)
    return lst_reversed_order
