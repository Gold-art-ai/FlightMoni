from django import forms

from .models import CrewAssignment, Flight, FlightAttendant, Gate, Terminal


class TerminalForm(forms.ModelForm):
    class Meta:
        model = Terminal
        fields = ["name", "city"]


class GateForm(forms.ModelForm):
    class Meta:
        model = Gate
        fields = ["terminal", "code", "is_active"]


class FlightAttendantForm(forms.ModelForm):
    class Meta:
        model = FlightAttendant
        fields = ["first_name", "last_name", "email", "phone", "employee_id", "rank", "languages"]


class FlightForm(forms.ModelForm):
    scheduled_time = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={"type": "datetime-local"}),
        input_formats=["%Y-%m-%dT%H:%M"],
    )

    class Meta:
        model = Flight
        fields = ["flight_number", "airline", "origin", "destination", "direction", "scheduled_time", "gate"]


class CrewAssignmentForm(forms.ModelForm):
    class Meta:
        model = CrewAssignment
        fields = ["flight", "attendant", "duty", "checked_in"]
