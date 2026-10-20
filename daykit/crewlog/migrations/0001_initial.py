# Generated manually for the DayKit airport demo.
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="FlightAttendant",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("first_name", models.CharField(max_length=80)),
                ("last_name", models.CharField(max_length=80)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("phone", models.CharField(blank=True, max_length=30)),
                ("employee_id", models.CharField(max_length=20, unique=True)),
                (
                    "rank",
                    models.CharField(
                        choices=[("junior", "Junior"), ("senior", "Senior"), ("lead", "Lead")],
                        default="junior",
                        max_length=30,
                    ),
                ),
                ("languages", models.CharField(help_text="Example: English, French, Kinyarwanda", max_length=160)),
            ],
            options={"ordering": ["last_name", "first_name"]},
        ),
        migrations.CreateModel(
            name="Terminal",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=80, unique=True)),
                ("city", models.CharField(default="Kigali", max_length=80)),
            ],
            options={"ordering": ["name"]},
        ),
        migrations.CreateModel(
            name="Gate",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("code", models.CharField(max_length=12)),
                ("is_active", models.BooleanField(default=True)),
                (
                    "terminal",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="gates", to="crewlog.terminal"),
                ),
            ],
            options={"ordering": ["terminal__name", "code"], "unique_together": {("terminal", "code")}},
        ),
        migrations.CreateModel(
            name="Flight",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("flight_number", models.CharField(max_length=12, unique=True)),
                ("airline", models.CharField(max_length=80)),
                ("origin", models.CharField(max_length=80)),
                ("destination", models.CharField(max_length=80)),
                ("direction", models.CharField(choices=[("arrival", "Arrival"), ("departure", "Departure")], max_length=12)),
                ("scheduled_time", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "gate",
                    models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="flights", to="crewlog.gate"),
                ),
            ],
            options={"ordering": ["scheduled_time"]},
        ),
        migrations.CreateModel(
            name="CrewAssignment",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "duty",
                    models.CharField(
                        choices=[("cabin", "Cabin"), ("boarding", "Boarding"), ("safety", "Safety"), ("service", "Service")],
                        max_length=30,
                    ),
                ),
                ("checked_in", models.BooleanField(default=False)),
                (
                    "attendant",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="assignments",
                        to="crewlog.flightattendant",
                    ),
                ),
                (
                    "flight",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="assignments", to="crewlog.flight"),
                ),
            ],
            options={"ordering": ["flight__scheduled_time", "duty"], "unique_together": {("flight", "attendant")}},
        ),
        migrations.AddField(
            model_name="flight",
            name="attendants",
            field=models.ManyToManyField(blank=True, related_name="flights", through="crewlog.CrewAssignment", to="crewlog.flightattendant"),
        ),
    ]
