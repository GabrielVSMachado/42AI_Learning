from sos import sos


def test_letter_A_expected_morse_code_for_A():
    assert sos('A') == '.-'


def test_letter_a_expected_morse_code_for_a():
    assert sos('a') == '.-'


def test_letter_B_expected_morse_code_for_b():
    assert sos('B') == '-...'


def test_letter_C_expected_morse_code_for_c():
    assert sos('C') == '-.-.'


def test_letter_D_expected_morse_code_for_D():
    assert sos('D') == '-..'


def test_letter_E_expected_morse_code_for_e():
    assert sos('E') == '.'


def test_letter_F_expected_morse_code_for_F():
    assert sos('F') == '..-.'


def test_letter_G_expected_morse_code_for_G():
    assert sos('G') == '--.'


def test_letter_H_expected_morse_code_for_H():
    assert sos('H') == '....'


def test_letter_I_expected_morse_code_for_I():
    assert sos('I') == '..'


def test_letter_J_expected_morse_code_for_J():
    assert sos('J') == '.---'


def test_letter_K_expected_morse_code_for_K():
    assert sos('K') == '-.-'


def test_letter_L_expected_morse_code_for_L():
    assert sos('L') == '.-..'


def test_letter_M_expected_morse_code_for_M():
    assert sos('M') == '--'


def test_letter_N_expected_morse_code_for_N():
    assert sos('N') == '-.'


def test_letter_O_expected_morse_code_for_O():
    assert sos('O') == '---'


def test_letter_P_expected_morse_code_for_P():
    assert sos('P') == '.--.'


def test_letter_Q_expected_morse_code_for_Q():
    assert sos('Q') == '--.-'


def test_letter_R_expected_morse_code_for_R():
    assert sos('R') == '.-.'


def test_letter_S_expected_morse_code_for_S():
    assert sos('S') == '...'


def test_letter_T_expected_morse_code_for_T():
    assert sos('T') == '-'


def test_letter_U_expected_morse_code_for_U():
    assert sos('U') == '..-'


def test_letter_V_expected_morse_code_for_V():
    assert sos('V') == '...-'


def test_letter_W_expected_morse_code_for_W():
    assert sos('W') == '.--'


def test_letter_X_expected_morse_code_for_X():
    assert sos('X') == '-..-'


def test_letter_Y_expected_morse_code_for_Y():
    assert sos('Y') == '-.--'


def test_letter_Z_expected_morse_code_for_Z():
    assert sos('Z') == '--..'


def test_letter_0_expected_morse_code_for_0():
    assert sos('0') == '-----'


def test_letter_1_expected_morse_code_for_1():
    assert sos('1') == '.----'


def test_letter_2_expected_morse_code_for_2():
    assert sos('2') == '..---'


def test_letter_3_expected_morse_code_for_3():
    assert sos('3') == '...--'


def test_letter_4_expected_morse_code_for_4():
    assert sos('4') == '....-'


def test_letter_5_expected_morse_code_for_5():
    assert sos('5') == '.....'


def test_letter_6_expected_morse_code_for_6():
    assert sos('6') == '-....'


def test_letter_7_expected_morse_code_for_7():
    assert sos('7') == '--...'


def test_letter_8_expected_morse_code_for_8():
    assert sos('8') == '---..'


def test_letter_9_expected_morse_code_for_9():
    assert sos('9') == '----.'


def test_string_SOS_expected_respectively_morse_code():
    assert sos("SOS") == '... --- ...'


def test_string_HELLO_expected_respectively_morse_code():
    assert sos("HELLO") == '.... . .-.. .-.. ---'


def test_str_96_BOULEVARD_expected_morse_code():
    assert sos("96 BOULEVARD") == '----. -.... / -... --- ..- .-.. . ...- .- .-. -..'


def test_HELLO_divide_by__WORLD_expected_Error_message():
    assert sos("HELLO / WORLD") == "Error"


def test_empty_str_expected_empty_str():
    assert sos("") == ''


def test_two_tested_strings_as_differents_args():
    assert sos("SOS", "HELLO") == "... --- ... / .... . .-.. .-.. ---"


def test_two_strings_as_differents_args():
    assert sos("96 BOULEVARD", "Bessiere") == """----. -.... / -... --- ..- .-.. . ...- .- .-. -..\
 / -... . ... ... .. . .-. ."""
