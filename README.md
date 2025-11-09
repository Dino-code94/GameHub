# GameHub

GameHub is a simple Django web application where users can browse games and comment on them.
Users can view all games on the homepage, open game detail pages, and if logged in — post comments.

## Features

- Homepage lists all games
- Each game links to `/game/<id>/`
- Logged in users can write comments
- Anonymous users see “You must be logged in to comment.”
- Login / Logout / Register via Django auth
- Admin panel at `/admin/`

## Installation

```bash
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

python manage.py createsuperuser

**commit message:**  
`Add installation and admin setup section`
```
## Models

**Game**
- title
- description
- cover image (optional)

**Comment**
- game (ForeignKey)
- user (ForeignKey)
- text
- created datetime

## Optional Sample Data (Games Seed)

```bash
python manage.py shell

from games.models import Game

games = [
    {"title":"Diablo II", "description":"Legendary dark fantasy ARPG."},
    {"title":"Oblivion", "description":"Massive open-world fantasy adventure."},
    {"title":"Age of Empires II", "description":"Classic medieval RTS strategy."},
    {"title":"World of Warcraft", "description":"Iconic MMORPG in Azeroth."},
    {"title":"The Witcher 3", "description":"Story-driven RPG with consequences."},
    {"title":"Path of Exile", "description":"Deep ARPG with crazy build system."},
]

for g in games:
    Game.objects.create(**g)
```
