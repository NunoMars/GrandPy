import json
from grandpyapp.process import grandPyWork
from grandpyapp import app


def test_grandPyWork():
    with open("wiki_found_page.json") as wiki_data:
        messages = json.load(wiki_data)

    messages_test = {'messages': [
        "Et donc tu veux savoir tout sur " +
        "OpenClassrooms",
        "Coquinou, quand même!" +
        "Et bein oui c'est a : " +
        "7 Cité Paradis, 75010 Paris, France",
        "Pas bête la bête!" +
        " Allez autre chose... Je te montre," +
        " une image vaux mieux que 1000 mots!!!",
        "Et a propos de ta demande et pour la petite" +
        " histoire :" + messages
        ],
        'position': {'lat': 48.8748465, 'lng': 2.3504873},
        'tag': 'OpenClassrooms'}
    assert grandPyWork("OpenClassrooms", app) == messages_test
