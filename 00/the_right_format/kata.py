def kata00():
    t = (10, 20, 30)
    return f"The 3 numbers are: {t[0]}, {t[1]}, {t[2]}"


def kata01():
    languages = {
            'Python':   'Guido van Rossum',
            'Ruby':     'Yukihiro Matsumoto',
            'PHP':      'Rasmus Lerdorf'
            }
    for i in languages:
        print(i + ' was created by ' + languages[i])


def kata02():
    time = (3, 30, 2019, 9, 25)
    return "%.2d/%d/%d %.2d:%d" % (time[3], time[4], time[2], time[0], time[1])


def kata03():
    string = "The right format"
    return string.rjust(42, '-')


def kata04():
    numbers = (0, 4, 132.422222, 10000, 12345.67)
    return "day_%.2d, ex_%.2d : " % (numbers[0], numbers[1]) +\
        "{0:.2f}, {1:.2e}, {2:.2e}".format(numbers[2], numbers[3], numbers[4])
