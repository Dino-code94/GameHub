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
