import requests
import json

# Api Gmaps


def call_google_maps_positionnement():
    """
    Send a request to Google Maps API
    """
    search_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    search_payload = {"key": "AIzaSyC4v_YJVsNLXGa0pXP6U3Lwp8WHPi1fnsc", "query": "openclassrooms"}
    search_req = requests.get(search_url, params=search_payload)
    search_json = search_req.json()

    with open('gmaps_data.json', 'w') as fp:
        json.dump(search_json, fp)


# Api Wikipedia


def call_wiki_main_page():
    """
    Call Api Wikipedia
    """
    s = requests.Session()
    url = "https://fr.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "list": "search",
        "srsearch": "{}".format("OpenClassrooms")
        }
    r = s.get(url=url, params=params)
    data = r.json()
    with open('wiki_tittle_main_page.json', 'w') as fp:
        json.dump(data, fp)
    print(data)


call_wiki_main_page()


def call_wiki_found_page():
    """
    Second request to wikipedia to have the text of the first request
    """
    s = requests.Session()

    url = "https://fr.wikipedia.org/w/api.php"
    params = {
        'action': "query",
        'pageids': 4338589,
        'format': "json",
        'prop': 'extracts',
        'explaintext': 1,
        'exsentences': 7,
    }
    r = s.get(url=url, params=params)
    data = r.json()

    text = data['query']['pages'][str(4338589)]['extract']

    with open('wiki_found_page.json', 'w') as fp:
        json.dump(text, fp)


