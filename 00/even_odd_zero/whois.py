def the_odd_even_or_zero(*args: int) -> str:
    '''Check if the number is Odd, Even or Zero and return a string
    which describe the case'''
    if (len(args) > 0):
        try:
            number = int(*args)
            if number & 0b1:
                return "I\'m Odd."
            elif not number:
                return "I\'m Zero."
            return "I\'m Even."
        except:
            return "ERROR"
    return None
