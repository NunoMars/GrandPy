import json

from grandpyapp.interface_requests import (
  call_google_maps_positionnement,
  call_wiki_main_page,
  call_wiki_found_page
)
from .config import API_PASSWORD



"""
For test all API's you need a Google DEV Key,
For security reasons i have hide in a Py secret file.
Here you must put Yours DEV Google key
"""

key = API_PASSWORD


def test_call_google_maps(monkeypatch):
    with open("gmaps_data.json") as g_maps_data:
        results_test = json.load(g_maps_data)

    def mock_g_maps(key, tittle):
        return results_test

    monkeypatch.setattr(
      "grandpyapp.interface_requests.call_google_maps_positionnement",
      mock_g_maps
      )
    assert call_google_maps_positionnement(
      key, "openclassrooms") == results_test


results_call_wiki_main_page = call_wiki_main_page(
      "openclassrooms")
with open("wiki_tittle_main_page.json", "w") as f_write:
    json.dump(results_call_wiki_main_page, f_write)


def test_call_wiki_main_page(monkeypatch):
    with open("wiki_tittle_main_page.json") as wiki_tittle_data:
        results_call_wiki_main_page = json.load(wiki_tittle_data)

    def mock_call_wiki_main_page(title):
        return results_call_wiki_main_page

    monkeypatch.setattr(
      "grandpyapp.interface_requests.call_wiki_main_page",
      mock_call_wiki_main_page
      )

    assert call_wiki_main_page("openclassrooms") == results_call_wiki_main_page


def test_call_wiki_found_page(monkeypatch):
    with open("wiki_found_page.json") as wiki_found_data:
        results_call_wiki_found_page = json.load(wiki_found_data)

    def mock_call_wiki_found_page(pageid):
        return results_call_wiki_found_page

    monkeypatch.setattr(
      "grandpyapp.interface_requests.call_wiki_found_page",
      mock_call_wiki_found_page
      )

    data = call_wiki_main_page("Openclassrooms")
    pageid = data["query"]["search"][0]["pageid"]

    assert call_wiki_found_page(pageid) == results_call_wiki_found_page
