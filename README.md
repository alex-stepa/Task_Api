# Task Api

REST API pro správu úkolů postavené na FastAPI.
Spuštění
bashpip install fastapi uvicorn
uvicorn main:app --reload
Server běží na http://127.0.0.1:8000.

**GET** /tasks – vrátí seznam všech úkolů

**GET** /tasks/{id} – vrátí jeden úkol podle ID

**POST** /tasks – vytvoří nový úkol

**PUT** /tasks/{id} – upraví existující úkol

**DELETE** /tasks/{id} – smaže úkol

**Příklady**

**POST /tasks**

Tělo požadavku:
json{ "title": "Nakoupit", "description": "Mléko, chléb", "done": false }

Odpověď 201:

json{ "id": 1, "title": "Nakoupit", "description": "Mléko, chléb", "done": false }

**PUT /tasks/1**

Tělo požadavku (stačí jen měněná pole):

json{ "done": true }

Odpověď 200:

json{ "id": 1, "title": "Nakoupit", "description": "Mléko, chléb", "done": true }

**DELETE /tasks/1**

Odpověď 200:

json{ "message": "Úkol 'Nakoupit' byl smazán" }

**Chyba – úkol nenalezen**

Odpověď 404:

json{ "detail": "Úkol s ID 99 nebyl nalezen" }

**Poznámky**

Data jsou uložena pouze v paměti – po restartu serveru se smažou.
