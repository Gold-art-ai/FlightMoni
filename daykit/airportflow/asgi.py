import os
import sys
from pathlib import Path

from django.core.asgi import get_asgi_application

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "airportflow.settings")

application = get_asgi_application()
