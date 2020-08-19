from grandpyapp.first_input_parser import parse_user_input as parse
from .config import STOP_WORDS


stop_words_custom = STOP_WORDS


def test_parse_user_input():
    test_user_input = "Bonjour GrandPy peut-tu me donner"\
        " l'adresse d'openclassrooms stp?"
    assert parse(
        test_user_input,
        stop_words_custom) == "openclassrooms"


def test_parse_user_input_empty():
    test_empty_user_input = " "
    assert parse(
        test_empty_user_input, stop_words_custom) == []
