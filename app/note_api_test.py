import requests

# Functie om alle notities ophalen te testen
def test_get_all_notes():
    response = requests.get('http://127.0.0.1:8000/notes')
    assert response.status_code == 200

# Functie om een specifieke notitie op basis van een id op te halen en te testen, in dit geval de eerste notitie
def test_get_first_note():
    # Voeg een dummy notitie toe
    dummy_note = {"title": "Dummy Title", "author": "Dummy Author", "content": "Dummy Content"}
    create_response = requests.post('http://127.0.0.1:8000/notes/', json=dummy_note)
    assert create_response.status_code == 200

    # Haal de eerste notitie op
    response = requests.get('http://127.0.0.1:8000/notes/1')
    assert response.status_code == 200
    assert response.json() != {}  # Niet leeg

# Functie om een notitite op te halen op basis van auteur te testen, bij deze voor 'Renzo'
def test_get_note_from_author_Renzo():
    # Voeg een dummy notitie toe
    dummy_note = {"title": "Dummy Title", "author": "Renzo", "content": "Dummy Content"}
    create_response = requests.post('http://127.0.0.1:8000/notes/', json=dummy_note)
    assert create_response.status_code == 200

    # Haal notities op basis van auteur 'Renzo'
    response = requests.get('http://127.0.0.1:8000/notes/author/Renzo')
    assert response.status_code == 200
    assert response.json() != []  # Niet leeg