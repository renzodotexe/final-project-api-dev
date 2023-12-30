import requests


# Functie om alle notities ophalen te testen
def test_get_all_notes():
    response = requests.get('http://127.0.0.1:8000/notes')
    assert response.status_code == 200


# Functie om een specifieke notitie ophalen te testen, in dit geval de eerste
def test_get_first_note():
    response = requests.get('http://127.0.0.1:8000/notes/1')
    assert response.status_code == 200