from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand

from crewlog.models import CrewAssignment, Flight, FlightAttendant, Gate, Terminal


ROLE_PERMISSIONS = {
    "Airport Manager": {
        Terminal: ["view", "add", "change", "delete"],
        Gate: ["view", "add", "change", "delete"],
        Flight: ["view", "add", "change", "delete"],
        FlightAttendant: ["view", "add", "change", "delete"],
        CrewAssignment: ["view", "add", "change", "delete"],
    },
    "Flight Dispatcher": {
        Terminal: ["view"],
        Gate: ["view", "add", "change"],
        Flight: ["view", "add", "change"],
        FlightAttendant: ["view"],
        CrewAssignment: ["view", "add", "change"],
    },
    "Crew Supervisor": {
        Terminal: ["view"],
        Gate: ["view"],
        Flight: ["view"],
        FlightAttendant: ["view", "add", "change"],
        CrewAssignment: ["view", "add", "change"],
    },
    "Read Only Operations": {
        Terminal: ["view"],
        Gate: ["view"],
        Flight: ["view"],
        FlightAttendant: ["view"],
        CrewAssignment: ["view"],
    },
}


class Command(BaseCommand):
    help = "Create Airport Flow admin groups with useful permissions."

    def handle(self, *args, **options):
        for group_name, model_permissions in ROLE_PERMISSIONS.items():
            group, _ = Group.objects.get_or_create(name=group_name)
            group.permissions.clear()

            for model, actions in model_permissions.items():
                content_type = ContentType.objects.get_for_model(model)
                permissions = Permission.objects.filter(
                    content_type=content_type,
                    codename__in=[f"{action}_{model._meta.model_name}" for action in actions],
                )
                group.permissions.add(*permissions)

            self.stdout.write(self.style.SUCCESS(f"Ready: {group_name}"))

        self.stdout.write(self.style.SUCCESS("Airport Flow roles are ready."))
