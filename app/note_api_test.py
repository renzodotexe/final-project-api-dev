import requests


def test_cleanup_database_before_testing():
    # Verwijder alle gegevens uit de database voordat de tests beginnen
    response = requests.delete('http://127.0.0.1:8000/reset-database')
    assert response.status_code == 200

def test_create_a_user():
    # Voeg een user toe aan de database
    response = requests.post('http://127.0.0.1:8000/users/', json={
        "email": "email@example.com",
        "password": "password"
    })
    assert response.status_code == 200


def test_create_a_note():
    # Voeg een notitie toe aan de database
    response = requests.post('http://127.0.0.1:8000/notes/', json={
        "title": "Test",
        "author": "Renzo",
        "content": "Dit is een test-notitie."
    })
    assert response.status_code == 200


# Functie om alle notities ophalen te testen
def test_get_all_notes():
    response = requests.get('http://127.0.0.1:8000/notes')
    assert response.status_code == 200
    assert response.json() != {}  # Niet leeg


# Functie om een specifieke notitie op basis van een id op te halen en te testen, in dit geval de eerste notitie
def test_get_note_by_id():
    response = requests.get('http://127.0.0.1:8000/notes/1')
    assert response.status_code == 200
    assert response.json() != {}  # Niet leeg


# Functie om een notitite op te halen op basis van auteur te testen, bij deze voor 'Renzo'
def test_get_note_by_author():
    response = requests.get('http://127.0.0.1:8000/notes/author/Renzo')
    assert response.status_code == 200
    assert response.json() != []  # Niet leeg


def test_update_note_by_id():
    # Voer de update uit
    update_data = {
        "title": "Updated Title",
        "content": "Updated Content"
    }
    update_response = requests.put('http://127.0.0.1:8000/notes/1', json=update_data)
    assert update_response.status_code == 200

    # Controleer of de notitie is bijgewerkt
    get_response = requests.get('http://127.0.0.1:8000/notes/1')
    assert get_response.status_code == 200
    updated_note = get_response.json()

    # Vergelijk de bijgewerkte gegevens
    assert updated_note['title'] == update_data['title']
    assert updated_note['content'] == update_data['content']
    assert updated_note['author'] == "Renzo"  # Author should remain unchanged


def test_delete_note_by_id():
    response = requests.delete('http://127.0.0.1:8000/notes/1')
    assert response.status_code == 200