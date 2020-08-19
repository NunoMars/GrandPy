import requests

# Api Gmaps


def call_google_maps_positionnement(key, tittle):
    """
    Send a request to Google Maps API
    """
    search_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    search_payload = {"key": key, "query": tittle}
    search_req = requests.get(search_url, params=search_payload)
    search_json = search_req.json()
    return search_json

# Api Wikipedia


def call_wiki_main_page(title):
    """
    Call Api Wikipedia
    """
    s = requests.Session()
    url = "https://fr.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "list": "search",
        "srsearch": "{}".format(title)
        }
    r = s.get(url=url, params=params)
    data = r.json()
    return data


def call_wiki_found_page(pageid):
    """
    Second request to wikipedia to have the text of the first request
    """
    s = requests.Session()

    url = "https://fr.wikipedia.org/w/api.php"
    params = {
        'action': "query",
        'pageids': pageid,
        'format': "json",
        'prop': 'extracts',
        'explaintext': 1,
        'exsentences': 6,
    }
    r = s.get(url=url, params=params)
    data = r.json()

    text = data['query']['pages'][str(pageid)]['extract']
    return text
