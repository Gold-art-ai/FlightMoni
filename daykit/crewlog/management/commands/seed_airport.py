from datetime import timedelta

from django.core.management.base import BaseCommand
from django.utils import timezone

from crewlog.models import CrewAssignment, Flight, FlightAttendant, Gate, Terminal


class Command(BaseCommand):
    help = "Create sample airport flights, gates, attendants, and duty assignments."

    def handle(self, *args, **options):
        terminal, _ = Terminal.objects.get_or_create(name="Terminal A", defaults={"city": "Kigali"})
        gate_a1, _ = Gate.objects.get_or_create(terminal=terminal, code="A1")
        gate_a2, _ = Gate.objects.get_or_create(terminal=terminal, code="A2")

        attendants = [
            ("FA-100", "Aline", "Mutesi", "lead", "English, French, Kinyarwanda"),
            ("FA-204", "Noah", "Kamanzi", "senior", "English, Swahili"),
            ("FA-311", "Iris", "Uwase", "junior", "English, French"),
        ]
        people = {}
        for employee_id, first, last, rank, languages in attendants:
            people[employee_id], _ = FlightAttendant.objects.get_or_create(
                employee_id=employee_id,
                defaults={
                    "first_name": first,
                    "last_name": last,
                    "rank": rank,
                    "languages": languages,
                    "email": f"{first.lower()}.{last.lower()}@airport.test",
                },
            )

        flight_one, _ = Flight.objects.get_or_create(
            flight_number="DK101",
            defaults={
                "airline": "DayKit Air",
                "origin": "Kigali",
                "destination": "Nairobi",
                "direction": Flight.DEPARTURE,
                "scheduled_time": timezone.now() + timedelta(minutes=40),
                "gate": gate_a1,
            },
        )
        flight_two, _ = Flight.objects.get_or_create(
            flight_number="DK210",
            defaults={
                "airline": "DayKit Air",
                "origin": "Doha",
                "destination": "Kigali",
                "direction": Flight.ARRIVAL,
                "scheduled_time": timezone.now() + timedelta(hours=2),
                "gate": gate_a2,
            },
        )

        CrewAssignment.objects.get_or_create(flight=flight_one, attendant=people["FA-100"], defaults={"duty": "boarding"})
        CrewAssignment.objects.get_or_create(flight=flight_one, attendant=people["FA-204"], defaults={"duty": "safety"})
        CrewAssignment.objects.get_or_create(
            flight=flight_two,
            attendant=people["FA-311"],
            defaults={"duty": "service", "checked_in": True},
        )

        self.stdout.write(self.style.SUCCESS("Airport demo data is ready."))
