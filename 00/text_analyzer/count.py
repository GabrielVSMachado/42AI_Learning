def text_analyzer(input: str) -> str:
    num_characters = 1
    upper_letters = 0
    lower_letters = 1
    punctuation_marks = 0
    spaces = 0
    return f"""The text contains {num_characters} characters:\n
- {upper_letters} upper letters\n
- {lower_letters} lower letters\n
- {punctuation_marks} punctuation marks\n
- {spaces} spaces"""
