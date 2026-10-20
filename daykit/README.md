# DayKit

A lightweight Python toolkit for everyday routines, time utilities, and simple productivity helpers.

## Installation

```bash
pip install daykit
```

> If the package name is already taken on PyPI, choose a unique distribution name before publishing.

## Quick Start

```python
from daykit import (
    good_morning,
    good_afternoon,
    good_evening,
    meal_time,
    get_greeting,
    format_duration,
    is_weekend,
    percentage,
)

print(good_morning("Ishara"))
print(meal_time(12))
print(get_greeting("Ishara", 18))
print(format_duration(125))
print(is_weekend())
print(percentage(45, 60))
```

## Features

- Time-aware greetings
- Meal-time messages
- Human-readable duration formatting
- Weekend detection
- Percentage calculations
- Simple study/productivity helpers
- Airport flight and attendant status helpers
- Type hints and validation
- Small, dependency-free API

## Django demo: Airport Flow

This repository also includes a simple but meaningful Django project:

- `airportflow` is the Django project.
- `crewlog` is the Django app for airport movement records.
- `daykit.airport` is the homemade package module used by the Django app.

The demo includes CRUD screens, multiple related tables, model inheritance, a many-to-many relationship through `CrewAssignment`, static CSS, and plain JavaScript.

Run it from this folder:

```bash
python -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_airport
python manage.py runserver
```

Then open:

```text
http://127.0.0.1:8000/
```

Useful Django commands:

```bash
python manage.py createsuperuser
python manage.py setup_airport_roles
python manage.py test
python manage.py makemigrations
```

Admin login:

```bash
python manage.py createsuperuser
python manage.py setup_airport_roles
python manage.py runserver
```

Open `http://127.0.0.1:8000/admin/`, log in with the superuser, then create staff users and place them into one of these groups:

- `Airport Manager`: full access to airport records.
- `Flight Dispatcher`: can manage flights, gates, and crew assignments.
- `Crew Supervisor`: can manage attendants and crew assignments.
- `Read Only Operations`: can view airport records without editing them.

## Development

Clone the repository, create a virtual environment, and install the package in editable mode:

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

macOS/Linux:

```bash
source .venv/bin/activate
```

Then:

```bash
python -m pip install --upgrade pip
pip install -e ".[dev]"
pytest
```

## Build the package

```bash
python -m pip install build
python -m build
```

The generated files will appear in `dist/`.

## License

MIT License. See `LICENSE`.
