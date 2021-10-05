def text_analyzer(text=None) -> str:
    """Return a string with the number of characters and other elements:
    number of upper_cases, lower_cases, punctuation_marks and spaces"""
    while text is None:
        print("What is the text to analyse?")
        text = input()
    num_characters = len(text)
    upper_letters = len([i for i in text if i.isupper()])
    lower_letters = len([i for i in text if i.islower()])
    spaces = len([i for i in text if i.isspace()])
    punctuation_marks = len([i for i in text if not (i.islower() or
                            i.isspace() or i.isupper() or i.isdigit())])
    return f"""The text contains {num_characters} characters:\n
- {upper_letters} upper letters\n
- {lower_letters} lower letters\n
- {punctuation_marks} punctuation marks\n
- {spaces} spaces"""
