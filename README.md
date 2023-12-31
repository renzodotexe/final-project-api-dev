# FastAPI Notities API (Eindproject)

## Beschrijving

Dit eindproject implementeert een RESTful API voor het beheren van notities met behulp van FastAPI. Het basisproject was gebaseerd op een blog, voor het eindproject werd dit een notitiesysteem.

### Volbrachte aanvullingen

- 2.1
- 2.2
- 3.1
- 3.1.1
- 3.1.2

## Hosting

### API

Deze API is gehost op Okteto Cloud. Je kunt de API-documentatie en voorbeelden vinden op de volgende locatie:

[Okteto Cloud Container](https://notes-api-renzodotexe.cloud.okteto.net/docs#/)

### Frontend

Deze API heeft ook een frontend en is gehost op Netlify. Je kunt deze uitproberen op de volgende locatie:

[Netlify Frontend](https://notes-api-renzodotexe.netlify.app)

## Aantoonbare Werking

Hieronder vind je screenshots die de werking van elk API-endpoint demonstreren.

### Weergeven Alle Notities

- **Alle Notities**
  ![Alle Notities](screenshots/get-all-notes-1.png)

### Aanmaken Nieuwe Notitie

- **Request Body**
  ![Verzoekbody](screenshots/create-note-1.png)
- **Succes**
  ![Succes](screenshots/create-note-2.png)
- **Fout bij duplicaat**
  ![Fout bij duplicaat](screenshots/create-note-3.png)
- **Verkeerd datatype**
  ![Verkeerd datatype](screenshots/create-note-4.png)

### Ophalen Specifieke Notitie (op ID)

- **Geldige ID**
  ![Geldige ID](screenshots/get-note-by-id-1.png)
- **Ongeldige ID**
  ![Ongeldige ID](screenshots/get-note-by-id-2.png)
- **Verkeerd datatype**
  ![Verkeerd datatype](screenshots/get-note-by-id-3.png)

### Bijwerken Notitie (op ID)

- **Originele Waarden**
  ![Originele Waarden](screenshots/update-note-by-id-1.png)
- **Gewijzigde Waarden**
  ![Gewijzigde Waarden](screenshots/update-note-by-id-2.png)

### Verwijderen Notitie (op ID)

- **Succes**
  ![Succes](screenshots/delete-note-1.png)
- **Fout bij ongeldige ID**
  ![Fout bij ongeldige ID](screenshots/delete-note-2.png)
- **Verkeerd Datatype**
  ![Verkeerd datatype](screenshots/delete-note-3.png)
- **Niet Geautoriseerd**
  ![Niet Geautoriseerd](screenshots/delete-note-4.png)

### Ophalen Specifieke Notitie (op Auteur)

- **Geldige Auteur**
  ![Geldige Auteur](screenshots/get-note-by-author-1.png)
- **Ongeldige Auteur**
  ![Ongeldige Auteur](screenshots/get-note-by-author-2.png)

### Reset Database

- **Succes**
  ![Succes](screenshots/reset-database-1.png)
- **Niet Geautoriseerd**
  ![Niet Geautoriseerd](screenshots/reset-database-2.png)
- **Bewijs**
  ![Bewijs](screenshots/reset-database-3.png)

### Aanmaken Nieuwe Gebruiker

- **Request Body**
  ![Verzoekbody](screenshots/create-user-1.png)
- **Succes**
  ![Succes](screenshots/create-user-2.png)
- **Fout bij duplicaat**
  ![Fout bij duplicaat](screenshots/create-user-3.png)
- **Verkeerd datatype**
  ![Verkeerd datatype](screenshots/create-user-4.png)

## Volledige OpenAPI Documentatie

Screenshots van de volledige OpenAPI-docs pagina:

- **Overzicht**
  ![Overzicht](screenshots/openapi-docs-1.png)
- **GET - Alle Notities**
  ![GET - Alle Notities](screenshots/openapi-docs-2.png)
- **POST - Nieuwe Notitie**
  ![POST - Nieuwe Notitie](screenshots/openapi-docs-3.png)
- **GET - Zoeken Notitie Op ID**
  ![GET - Zoeken Notitie Op ID](screenshots/openapi-docs-4.png)
- **PUT - Bijwerken Notitie Op ID**
  ![PUT - Bijwerken Notitie Op ID](screenshots/openapi-docs-5.png)
- **DELETE - Verwijderen Notitie Op ID**
  ![DELETE - Verwijderen Notitie Op ID](screenshots/openapi-docs-6.png)
- **GET - Zoeken Notitie Op Auteur**
  ![GET - Zoeken Notitie Op Auteur](screenshots/openapi-docs-7.png)
- **DELETE - Volledige Database Reset**
  ![DELETE - Volledige Database Reset](screenshots/openapi-docs-8.png)
- **POST - Nieuwe Gebruiker**
  ![POST - Nieuwe Gebruiker](screenshots/openapi-docs-9.png)
- **POST - Login Access Token**
  ![POST - Login Access Token](screenshots/openapi-docs-10.png)
