from .first_input_parser import parse_user_input
from .interface_requests import (
    call_google_maps_positionnement,
    call_wiki_main_page,
    call_wiki_found_page
)


def grandPyWork(message, app):
    """
    Function, to prepare the answers and instace all API's once.
    """
    # Config options
    app.config.from_object('config')
    # To get one variable, tape app.config['MY_VARIABLE']
    g_maps_key = app.config["MAPS_API_KEY"]
    stop_words_custom = app.config['STOP_WORDS']
    # Parse the input sentence
    parsed_msg = parse_user_input(message, stop_words_custom)

    # Request and test the Google Maps call
    msg_gmaps = call_google_maps_positionnement(
        g_maps_key,
        parsed_msg
        )
    try:
        location = msg_gmaps["results"][0]["geometry"]["location"]
    except IndexError or KeyError:
        ups = {"messages": [
            "Desolé je n'ai pas pu t'aider mon petit...",
            "Écris mieux tête de linotte!",
            "Et tu sait? A mon age, on n'a pas toute sa tête!",
            "Et redemande moi-ce que tu veux, mais tu t'appliques ok?"
        ], "tag": "ups"
        }
        return ups
    else:
        address = msg_gmaps["results"][0]["formatted_address"]
    # call Wikipedia for a tittle and test il the parsed input is Ok
    wiki_title = call_wiki_main_page(parsed_msg)
    try:
        processed_title = wiki_title["query"]["search"][0]["title"]
    except IndexError or KeyError:
        return {"messages ": [
            "Ups je n'ai pas trouvé ce que tu me demandes,",
            "On vas devoir changer de conversation, tu veux?",
            "J'ai bien cherché dans ma tête, mais rien!!",
            "je ne vois pas de quoi tu veux parler.."
        ]}
    else:
        pageid = wiki_title["query"]["search"][0]["pageid"]
        history = call_wiki_found_page(pageid)
        try:
            # Construction of the bot responses
            message = {
                "messages": [
                            "Et donc tu veux savoir tout sur " +
                            processed_title,
                            "Coquinou, quand même!" +
                            "Et bein oui c'est a : " + address,
                            "Pas bête la bête!" +
                            " Allez autre chose... Je te montre," +
                            " une image vaux mieux que 1000 mots!!!",
                            "Et a propos de ta demande et pour la petite" +
                            " histoire :" + history
                            ],
                "position": location,
                "tag": processed_title
                }
            return message
        except TypeError:
            return {"messages": [
                "T'as pas honte de faire une blague a PAPPY?",
                "A ton age!!",
                "Ups je n'ai pas trouvé ce que tu me demandes,",
                "On vas devoir changer de conversation, " +
                ".... Ha ces jetits jeunes...!!!"
            ]}
