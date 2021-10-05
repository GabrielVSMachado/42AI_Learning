def text_analyzer(input: str) -> str:
    """Return a string with the number of characters and other elements:
    number of upper_cases, lower_cases, punctuation_marks and spaces"""
    num_characters = len(input)
    upper_letters = len([i for i in input if i.isupper()])
    lower_letters = len([i for i in input if i.islower()])
    spaces = len([i for i in input if i.isspace()])
    punctuation_marks = num_characters - (spaces +
                                          upper_letters + lower_letters)
    return f"""The text contains {num_characters} characters:\n
- {upper_letters} upper letters\n
- {lower_letters} lower letters\n
- {punctuation_marks} punctuation marks\n
- {spaces} spaces"""
