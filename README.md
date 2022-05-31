# MovieRecommendationApp
### Prototyp aplikacji MovieRecommendationApp


## Spis Treści
* [Technologie](#technologie)
* [Tasks](#tasks)
* [Struktura katalogów](#struktura-katalogów)
* [Setup](#Setup)


## Technologie
Wykorzystane technologie w projekcie:
- Python 3.10.4
- Django 4.0.4
- Bootstrap 5.2.0
- Bootstrap Icons 1.8.0
- MDB 4.1.0

## Tasks
- [x] Skonfigurowanie widoku bazowego (base/)
- [x] Skonfigurowanie widoku strony głównej (home/)
- [x] Skonfigurowanie widoku profilu użytkownika (user/)
    - [x] Skonfigurowanie widoku listy "Watched"
    - [x] Skonfigurowanie widoku listy "Recommended"
- [x] Skonfigurowanie widoku wszystkich filmów (browse/)

## Struktura katalogów
```
├── app                     # Documentation files (alternatively `doc`)
│   ├── __pycache__         # Table of contents
│   ├── templates           # Widoki HTML
│       ├── base.html       # Widok HTML dla struktury bazowej projektu (navbar + footer)
│       ├── browse.html     # Widok HTML dla przeglądarki filmów
│       ├── home.html       # Widok HTML dla strony głównej
│       ├── user.html       # Widok HTML dla profilu użytkownika
│   ├── __init__.py         # Pusty plik Pythona który mówi, że ten katalog powinien byc uważany za pakiet Pythona
│   ├── asgi.py             # Punkt wejściowy dla serwerów WWW kompatybilnych z ASGI
│   ├── settings.py         # Ustawienia i konfiguracja dla projektu Django
│   ├── urls.py             # Deklaracje URL-i dla projektu
│   ├── views.py            # Widok, logika aplikacji
│   ├── wsgi.py             # Punkt wejściowy dla serwerów WWW kompatybilnych z WSGI
├── db.sqlite3              # Baza SQLite
├── manage.py               # Narzędzie linii komend
├── README.md               
```

## Instalacja 
Na samym początku trzeba się upewnić czy mamy zainstalowanego Pythona, jeżeli tak to uruchamiamy następujące komendy: 

```
git clone https://github.com/wiluszdamian/MovieRecommendationApp.git

cd MovieRecommendationApp

pip install -r requirements.txt

python manage.py runserver
```

Aplikacja poda w konsoli informacje na jakim porcie się uruchamia