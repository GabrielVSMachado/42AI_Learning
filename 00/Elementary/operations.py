def operations(*args):
    """
Usage: python operations.py <number1> <number2>
Example:
    python operations.py 10 3"""
    if len(args) == 0:
        return operations.__doc__
    elif len(args) > 2:
        return "InputError: too many arguments\n" + operations.__doc__
    try:
        number1 = int(args[0])
        number2 = int(args[1])
        try:
            quotient = number1 / number2
            remainder = number1 % number2
        except:
            quotient = "ERROR (div by zero)"
            remainder = "ERROR (modulo by zero)"
    except:
        return "InputError: only numbers\n" + operations.__doc__
    return f"""
Sum:        {sum(args)}
Difference: {number1 - number2}
Product:    {number1 * number2}
Quotient:   {quotient}
Remainder:  {remainder}"""
