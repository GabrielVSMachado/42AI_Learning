def sos(*args) -> str:
    morse_code_alphabet = {
            'A': '.-',
            'B': '-...',
            'C': '-.-.',
            'D': '-..',
            'E': '.',
            'F': '..-.',
            'G': '--.',
            'H': '....',
            'I': '..',
            'J': '.---',
            'K': '-.-',
            'L': '.-..',
            'M': '--',
            'N': '-.',
            'O': '---',
            'P': '.--.',
            'Q': '--.-',
            'R': '.-.',
            'S': '...',
            'T': '-',
            'U': '..-',
            'V': '...-',
            'W': '.--',
            'X': '-..-',
            'Y': '-.--',
            'Z': '--..',
            '0': '-----',
            '1': '.----',
            '2': '..---',
            '3': '...--',
            '4': '....-',
            '5': '.....',
            '6': '-....',
            '7': '--...',
            '8': '---..',
            '9': '----.'
            }
    to_morse = ' '.join([*args])
    message_in_morse_code = []
    for letter_offset in range(len(to_morse)):
        try:
            if to_morse[letter_offset] == " ":
                message_in_morse_code.append("/")
                continue
            message_in_morse_code.append(morse_code_alphabet[to_morse[letter_offset].upper()])
        except KeyError:
            return "Error"
    message_in_morse_code = ' '.join(message_in_morse_code)
    return message_in_morse_code
