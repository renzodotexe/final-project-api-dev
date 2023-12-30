import requests


def test_cleanup_database_before_testing():
    # Verwijder alle gegevens uit de database voordat de tests beginnen
    response = requests.delete('http://127.0.0.1:8000/reset-database')
    assert response.status_code == 200


def test_create_dummy_note_before_testing():
    # Voeg een notitie toe aan de database voordat de tests beginnen
    response = requests.post('http://127.0.0.1:8000/notes/', json={
        "title": "Test",
        "author": "Renzo",
        "content": "Dit is een testnotitie"
    })
    assert response.status_code == 200


# Functie om alle notities ophalen te testen
def test_get_all_notes():
    response = requests.get('http://127.0.0.1:8000/notes')
    assert response.status_code == 200


# Functie om een specifieke notitie op basis van een id op te halen en te testen, in dit geval de eerste notitie
def test_get_first_note():
    response = requests.get('http://127.0.0.1:8000/notes/1')
    assert response.status_code == 200
    assert response.json() != {}  # Niet leeg


# Functie om een notitite op te halen op basis van auteur te testen, bij deze voor 'Renzo'
def test_get_note_from_author_Renzo():
    response = requests.get('http://127.0.0.1:8000/notes/author/Renzo')
    assert response.status_code == 200
    assert response.json() != []  # Niet leeg
