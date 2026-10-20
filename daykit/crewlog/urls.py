from django.urls import path

from . import views

app_name = "crewlog"

urlpatterns = [
    path("", views.DashboardView.as_view(), name="dashboard"),
    path("flights/", views.FlightListView.as_view(), name="flight_list"),
    path("flights/new/", views.FlightCreateView.as_view(), name="flight_create"),
    path("flights/<int:pk>/", views.FlightDetailView.as_view(), name="flight_detail"),
    path("flights/<int:pk>/edit/", views.FlightUpdateView.as_view(), name="flight_update"),
    path("flights/<int:pk>/delete/", views.FlightDeleteView.as_view(), name="flight_delete"),
    path("attendants/", views.AttendantListView.as_view(), name="attendant_list"),
    path("attendants/new/", views.AttendantCreateView.as_view(), name="attendant_create"),
    path("attendants/<int:pk>/", views.AttendantDetailView.as_view(), name="attendant_detail"),
    path("attendants/<int:pk>/edit/", views.AttendantUpdateView.as_view(), name="attendant_update"),
    path("attendants/<int:pk>/delete/", views.AttendantDeleteView.as_view(), name="attendant_delete"),
    path("assignments/", views.AssignmentListView.as_view(), name="assignment_list"),
    path("assignments/new/", views.AssignmentCreateView.as_view(), name="assignment_create"),
    path("assignments/<int:pk>/edit/", views.AssignmentUpdateView.as_view(), name="assignment_update"),
    path("assignments/<int:pk>/delete/", views.AssignmentDeleteView.as_view(), name="assignment_delete"),
    path("terminals/new/", views.TerminalCreateView.as_view(), name="terminal_create"),
    path("gates/new/", views.GateCreateView.as_view(), name="gate_create"),
]
