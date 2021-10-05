from count import text_analyzer


def string_result(number_characters, up_letter, low_letter,
                  punctuation, spaces):
    return """The text contains {} characters:\n
- {} upper letters\n
- {} lower letters\n
- {} punctuation marks\n
- {} spaces""".format(number_characters, up_letter, low_letter,
                      punctuation, spaces)


def test_one_character_lower_case():
    assert text_analyzer('a') == string_result(1, 0, 1, 0, 0)


def test_one_character_upper_case():
    assert text_analyzer('A') == string_result(1, 1, 0, 0, 0)


def test_one_lower_and_one_upper():
    assert text_analyzer('aA') == string_result(2, 1, 1, 0, 0)


def test_ten_character_lower_case():
    assert text_analyzer('gabrielvit') == string_result(10, 0, 10, 0, 0)


def test_one_coma_character():
    assert text_analyzer(',') == string_result(1, 0, 0, 1, 0)


def test_coma_with_space():
    assert text_analyzer(', ') == string_result(2, 0, 0, 1, 1)


def ultimate_3_paragraphs_lore_ipsum():
    assert text_analyzer("""
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. In eu orci augue. Aliquam a rutrum massa. Donec non justo nunc. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Pellentesque at justo ut libero maximus dignissim id et elit. In faucibus dui ex, nec rhoncus est rutrum quis. Vivamus non bibendum leo, nec mollis nisi. Quisque scelerisque vulputate eros, vel varius magna. Quisque mauris nisi, pellentesque vitae luctus a, cursus sit amet tellus. Suspendisse eu consequat orci. Nam sit amet magna sed urna hendrerit ultricies. Aenean nunc elit, pulvinar in gravida a, luctus quis magna. Proin et sapien iaculis, euismod risus nec, vulputate nisl. Ut convallis elementum nisl et tempus.
            Fusce in nisi mi. Praesent ut magna vestibulum, imperdiet nunc id, sodales nisi. Phasellus laoreet sapien a mauris tristique, non commodo lorem varius. Nullam vitae tincidunt nibh, non varius ipsum. Sed ornare efficitur mi nec placerat. Etiam sed sem vel libero ultricies pharetra sed nec nibh. In dignissim, lorem ultricies hendrerit lacinia, magna risus efficitur ex, in pretium lorem magna sed lacus. Praesent rhoncus quis sapien nec bibendum. Cras aliquam molestie purus sit amet ornare. Aliquam aliquet volutpat elit, sed rhoncus ante. In luctus, purus eu hendrerit rutrum, elit arcu molestie metus, sit amet sodales ante augue a felis. Aenean cursus tincidunt faucibus. Curabitur aliquet convallis euismod.
            Vestibulum scelerisque efficitur velit at consequat. Aenean nibh ante, tempor ut ultricies nec, accumsan et nibh. Curabitur elementum sem sit amet mi tempor, vitae vestibulum justo luctus. Duis at metus elit. Nam vel massa mauris. Praesent sit amet augue malesuada orci tempor finibus. Donec aliquam sit amet lectus ac volutpat. Nullam placerat orci at ex maximus dignissim. Mauris eget ligula ultricies, iaculis augue a, lacinia odio. Quisque vel accumsan lacus. Donec tincidunt eget est vel sollicitudin. Suspendisse condimentum, lorem sed sollicitudin fermentum, urna ipsum aliquet magna, sed bibendum nulla erat et metus. Suspendisse consectetur neque ac urna mattis aliquam.""") == string_result(2126, 41, 1691, 71, 323)


def test_my_name():
    assert text_analyzer("""gabriel vitor sales machado""") == string_result(27, 0, 24, 0, 3)


def test_pdf_first_input():
    assert text_analyzer("""Python 2.0, released 2000, introduced
features like List comprehensions and a garbage collection
system capable of collecting reference cycles.""") == string_result(143, 2, 113, 4, 18)


def test_pdf_second_input():
    assert text_analyzer("""Python is an interpreted, high-level,
general-purpose programming language. Created by Guido
van Rossum and first released in 1991, Python\'s design philosophy
emphasizes code readability with its notable use of significant
whitespace.""") == string_result(234, 5, 187, 8, 30)
