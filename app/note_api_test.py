import requests
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


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


def test_create_new_note():
    new_note = {
        "title": "Test Title",
        "author": "Test Author",
        "content": "Test Content"
    }
    response = client.post("/notes/", json=new_note)
    assert response.status_code == 200
    assert response.json()["title"] == new_note["title"]


def test_update_note_by_id():
    note_id = 1
    updated_note = {
        "title": "Updated Title",
        "content": "Updated Content"
    }
    response = client.put(f"/notes/{note_id}", json=updated_note)
    assert response.status_code == 200
    assert response.json()["title"] == updated_note["title"]
    assert response.json()["content"] == updated_note["content"]
