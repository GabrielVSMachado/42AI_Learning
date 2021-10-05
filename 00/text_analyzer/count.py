def text_analyzer(text=None, *args) -> str:
    """Return a string with the number of characters and other elements:
    number of upper_cases, lower_cases, punctuation_marks and spaces"""
    if len(args) != 0:
        return "ERROR"
    while text is None:
        text = input("What is the text to analyse?\n")
    punctuation_marks = len([i for i in text if not (i.islower() or
                            i.isspace() or i.isupper() or i.isdigit())])
    return f"""The text contains {len(text)} characters:\n
- {len([i for i in text if i.isupper()])} upper letters\n
- {len([i for i in text if i.islower()])} lower letters\n
- {punctuation_marks} punctuation marks\n
- {len([i for i in text if i.isspace()])} spaces"""
