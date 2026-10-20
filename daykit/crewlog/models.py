from django.db import models
from django.urls import reverse
from django.utils import timezone

from daykit import attendant_load, movement_signal


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Person(TimeStampedModel):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=30, blank=True)

    class Meta:
        abstract = True

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Terminal(TimeStampedModel):
    name = models.CharField(max_length=80, unique=True)
    city = models.CharField(max_length=80, default="Kigali")

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


class Gate(TimeStampedModel):
    terminal = models.ForeignKey(Terminal, on_delete=models.CASCADE, related_name="gates")
    code = models.CharField(max_length=12)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["terminal__name", "code"]
        unique_together = ["terminal", "code"]

    def __str__(self) -> str:
        return f"{self.terminal.name}-{self.code}"


class FlightAttendant(Person):
    employee_id = models.CharField(max_length=20, unique=True)
    rank = models.CharField(
        max_length=30,
        choices=[
            ("junior", "Junior"),
            ("senior", "Senior"),
            ("lead", "Lead"),
        ],
        default="junior",
    )
    languages = models.CharField(max_length=160, help_text="Example: English, French, Kinyarwanda")

    class Meta:
        ordering = ["last_name", "first_name"]

    def __str__(self) -> str:
        return f"{self.full_name} ({self.employee_id})"

    def get_absolute_url(self):
        return reverse("crewlog:attendant_detail", args=[self.pk])

    @property
    def roster_label(self) -> str:
        return attendant_load(self.assignments.count())


class Flight(TimeStampedModel):
    ARRIVAL = "arrival"
    DEPARTURE = "departure"

    flight_number = models.CharField(max_length=12, unique=True)
    airline = models.CharField(max_length=80)
    origin = models.CharField(max_length=80)
    destination = models.CharField(max_length=80)
    direction = models.CharField(
        max_length=12,
        choices=[
            (ARRIVAL, "Arrival"),
            (DEPARTURE, "Departure"),
        ],
    )
    scheduled_time = models.DateTimeField(default=timezone.now)
    gate = models.ForeignKey(Gate, on_delete=models.PROTECT, related_name="flights")
    attendants = models.ManyToManyField(
        FlightAttendant,
        through="CrewAssignment",
        related_name="flights",
        blank=True,
    )

    class Meta:
        ordering = ["scheduled_time"]

    def __str__(self) -> str:
        return f"{self.flight_number} {self.origin} to {self.destination}"

    def get_absolute_url(self):
        return reverse("crewlog:flight_detail", args=[self.pk])

    @property
    def crew_checked_in(self) -> bool:
        assignments = self.assignments.all()
        return assignments.exists() and all(item.checked_in for item in assignments)

    @property
    def signal(self):
        return movement_signal(self.direction, self.scheduled_time, self.crew_checked_in)


class CrewAssignment(TimeStampedModel):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name="assignments")
    attendant = models.ForeignKey(FlightAttendant, on_delete=models.CASCADE, related_name="assignments")
    duty = models.CharField(
        max_length=30,
        choices=[
            ("cabin", "Cabin"),
            ("boarding", "Boarding"),
            ("safety", "Safety"),
            ("service", "Service"),
        ],
    )
    checked_in = models.BooleanField(default=False)

    class Meta:
        ordering = ["flight__scheduled_time", "duty"]
        unique_together = ["flight", "attendant"]

    def __str__(self) -> str:
        if not self.flight_id or not self.attendant_id:
            return "Crew assignment"
        return f"{self.attendant.full_name} on {self.flight.flight_number}"
