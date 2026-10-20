# DayKit — Project Repository

This repository contains the **DayKit** Python package and a full Django demo application that uses it.

## Repository Structure

| Path | Description |
|---|---|
| `src/` | The `daykit` Python package (published to TestPyPI) |
| `airportflow/` | The Django project configuration |
| `crewlog/` | The Django app for airport movement records |
| `tests/` | Unit tests for the `daykit` package |

---

## The `daykit` Package

A lightweight, dependency-free Python toolkit for everyday routines, time utilities, and productivity helpers.

**Install from TestPyPI:**

```bash
pip install -i https://test.pypi.org/simple/ daykit
```

**Quick example:**

```python
from daykit import get_greeting, format_duration, is_weekend, percentage

print(get_greeting("Ishara", 18))  # evening greeting
print(format_duration(125))        # "2 min 5 s"
print(is_weekend())                # True or False for today
print(percentage(45, 60))          # 75.0
```

See [`src/README.md`](src/README.md) for the full API reference.

---

## Django Demo: Airport Flow

A full-featured Django web application built on top of `daykit.airport`. It showcases:

- CRUD screens for airports, flights, gates, and crew
- Model inheritance and a many-to-many relationship via `CrewAssignment`
- Role-based access control using Django Groups
- Static CSS and plain JavaScript UI

### Run the Demo

From the repository root, with a virtual environment activated:

```bash
python -m venv .venv
```

| Windows | macOS / Linux |
|---|---|
| `.venv\Scripts\activate` | `source .venv/bin/activate` |

Then:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_airport
python manage.py runserver
```

Open <http://127.0.0.1:8000/>.

### Admin & Roles

```bash
python manage.py createsuperuser
python manage.py setup_airport_roles
```

Log in at <http://127.0.0.1:8000/admin/> and assign staff users to one of these groups:

| Group | Access |
|---|---|
| Airport Manager | Full access to all airport records |
| Flight Dispatcher | Manage flights, gates, and crew assignments |
| Crew Supervisor | Manage attendants and crew assignments |
| Read Only Operations | View records without editing |

Other useful commands:

```bash
python manage.py test
python manage.py makemigrations
```

---

## Development (Package)

```bash
cd src
pip install -e ".[dev]"
pytest
```

To build the distribution:

```bash
python -m pip install build
python -m build
```

The wheel and source archive are written to `src/dist/`.

---

## License

MIT License. See [`LICENSE`](LICENSE).
