from grandpyapp.process import grandPyWork
from grandpyapp import app


def test_grandPyWork():

    messages_test = {'messages': [
        'Et donc tu veux savoir tout sur Tour Eiffel',
        "Coquinou, quand même!Et bein oui c'est a : Champ de Mars, 5 Avenue" +
        " Anatole France, 75007 Paris, France",
        "Pas bête la bête! Allez autre chose... " +
        "Je te montre, une image vaux mieux" +
        " que 1000 mots!!!",
        "Et a propos de ta demande et pour la petite histoire " +
        ":La tour Eiffel  est une tour de fer puddlé de 324 mètres" +
        " de hauteur (avec antennes) située à Paris," +
        " à l’extrémité nord-ouest du parc du Champ-de-Mars" +
        " en bordure de la Seine dans le 7e arrondissement." +
        " Son adresse officielle est 5, avenue Anatole-France." +
        " Construite par Gustave Eiffel et ses collaborateurs pour" +
        " l’Exposition universelle de Paris de 1889, et initialement" +
        " nommée « tour de 300 mètres », ce monument est devenu le " +
        "symbole de la capitale française, et un site touristique de " +
        "premier plan : il s’agit du troisième site culturel français" +
        " payant le plus visité en 2015, avec 6,9 millions de visiteurs," +
        " en 2011 la cathédrale Notre-Dame de Paris était en tête des " +
        "monuments à l'accès libre avec 13,6 millions de visiteurs estimés" +
        " mais il reste le monument payant le plus visité au monde,. Depuis" +
        " son ouverture au public, elle a accueilli plus de 300 millions de" +
        " visiteurs.\nD’une hauteur de 312 mètres " +
        "à l’origine, la tour Eiffel " +
        "est restée le monument le plus élevé du monde" +
        " pendant quarante ans. Le" +
        " second niveau du troisième étage, appelé parfois quatrième étage," +
        " situé à 279,11 mètres, est la plus haute plateforme" +
        " d'observation" +
        " accessible au public de l'Union européenne et la" +
        " deuxième plus haute" +
        " d'Europe, derrière la tour Ostankino à Moscou culminant" +
        " à 337 mètres."
        ],
        'position': {'lat': 48.85837009999999, 'lng': 2.2944813},
        'tag': 'Tour Eiffel'}
    assert grandPyWork("tour eiffel", app) == messages_test
