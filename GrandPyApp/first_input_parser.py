import re
import string


def parse_user_input(user_input, stop_words_custom):
    """
    Get and parse user's sentences.
    """
    _punctuation = set(string.punctuation)
    for punct in set(user_input).intersection(_punctuation):
        user_input = user_input.replace(punct, ' ')
    user_input = ' '.join(user_input.split())

    user_input = re.split(",|'| |-|;", user_input)
    user_input = [x.lower() for x in user_input]
    new_sentence = []

    for word in user_input:
        if word not in stop_words_custom:
            new_sentence.append(word)
    result = ' '.join(new_sentence)

    return result


if __name__ == "__main__":
    from GrandPyApp.views import stop_words_custom

    print("Salut, je suis GrandPy, je suis là afin de t'aider ;-)")

    user_input = input('Que veux-tu savoir mon enfant?  :  ')
    parsed_user_input = parse_user_input(user_input, stop_words_custom)

    print("terminé, prêt pour requête : ", parsed_user_input)
