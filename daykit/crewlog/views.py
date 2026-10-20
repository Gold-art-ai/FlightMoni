from django.db.models import Count, Q
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, TemplateView, UpdateView

from .forms import CrewAssignmentForm, FlightAttendantForm, FlightForm, GateForm, TerminalForm
from .models import CrewAssignment, Flight, FlightAttendant, Gate, Terminal


class FormTitleMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        action = "Edit" if self.object else "Add"
        context["page_title"] = f"{action} {self.model._meta.verbose_name}"
        return context


class DashboardView(TemplateView):
    template_name = "crewlog/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["flights"] = Flight.objects.select_related("gate", "gate__terminal").prefetch_related("assignments")[:6]
        context["attendants"] = FlightAttendant.objects.annotate(load=Count("assignments"))[:5]
        context["open_assignments"] = CrewAssignment.objects.filter(checked_in=False).count()
        context["departures"] = Flight.objects.filter(direction=Flight.DEPARTURE).count()
        context["arrivals"] = Flight.objects.filter(direction=Flight.ARRIVAL).count()
        return context


class FlightListView(ListView):
    model = Flight
    template_name = "crewlog/flight_list.html"
    context_object_name = "flights"

    def get_queryset(self):
        queryset = Flight.objects.select_related("gate", "gate__terminal").prefetch_related("assignments")
        query = self.request.GET.get("q", "").strip()
        if query:
            queryset = queryset.filter(
                Q(flight_number__icontains=query)
                | Q(airline__icontains=query)
                | Q(origin__icontains=query)
                | Q(destination__icontains=query)
            )
        return queryset


class FlightDetailView(DetailView):
    model = Flight
    template_name = "crewlog/flight_detail.html"

    def get_queryset(self):
        return Flight.objects.select_related("gate", "gate__terminal").prefetch_related("assignments__attendant")


class FlightCreateView(FormTitleMixin, CreateView):
    model = Flight
    form_class = FlightForm
    template_name = "crewlog/form.html"


class FlightUpdateView(FormTitleMixin, UpdateView):
    model = Flight
    form_class = FlightForm
    template_name = "crewlog/form.html"


class FlightDeleteView(DeleteView):
    model = Flight
    template_name = "crewlog/confirm_delete.html"
    success_url = reverse_lazy("crewlog:flight_list")


class AttendantListView(ListView):
    model = FlightAttendant
    template_name = "crewlog/attendant_list.html"
    context_object_name = "attendants"

    def get_queryset(self):
        return FlightAttendant.objects.annotate(load=Count("assignments"))


class AttendantDetailView(DetailView):
    model = FlightAttendant
    template_name = "crewlog/attendant_detail.html"

    def get_queryset(self):
        return FlightAttendant.objects.prefetch_related("assignments__flight")


class AttendantCreateView(FormTitleMixin, CreateView):
    model = FlightAttendant
    form_class = FlightAttendantForm
    template_name = "crewlog/form.html"


class AttendantUpdateView(FormTitleMixin, UpdateView):
    model = FlightAttendant
    form_class = FlightAttendantForm
    template_name = "crewlog/form.html"


class AttendantDeleteView(DeleteView):
    model = FlightAttendant
    template_name = "crewlog/confirm_delete.html"
    success_url = reverse_lazy("crewlog:attendant_list")


class AssignmentListView(ListView):
    model = CrewAssignment
    template_name = "crewlog/assignment_list.html"
    context_object_name = "assignments"
    queryset = CrewAssignment.objects.select_related("flight", "attendant")


class AssignmentCreateView(FormTitleMixin, CreateView):
    model = CrewAssignment
    form_class = CrewAssignmentForm
    template_name = "crewlog/form.html"
    success_url = reverse_lazy("crewlog:assignment_list")


class AssignmentUpdateView(FormTitleMixin, UpdateView):
    model = CrewAssignment
    form_class = CrewAssignmentForm
    template_name = "crewlog/form.html"
    success_url = reverse_lazy("crewlog:assignment_list")


class AssignmentDeleteView(DeleteView):
    model = CrewAssignment
    template_name = "crewlog/confirm_delete.html"
    success_url = reverse_lazy("crewlog:assignment_list")


class TerminalCreateView(FormTitleMixin, CreateView):
    model = Terminal
    form_class = TerminalForm
    template_name = "crewlog/form.html"
    success_url = reverse_lazy("crewlog:dashboard")


class GateCreateView(FormTitleMixin, CreateView):
    model = Gate
    form_class = GateForm
    template_name = "crewlog/form.html"
    success_url = reverse_lazy("crewlog:dashboard")
