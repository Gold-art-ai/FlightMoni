from django.contrib import admin

from .models import CrewAssignment, Flight, FlightAttendant, Gate, Terminal

admin.site.site_header = "Airport Flow Admin"
admin.site.site_title = "Airport Flow"
admin.site.index_title = "Operations control"


class CrewAssignmentInline(admin.TabularInline):
    model = CrewAssignment
    extra = 1


@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = ["flight_number", "airline", "direction", "scheduled_time", "gate", "crew_checked_in"]
    list_filter = ["direction", "gate__terminal"]
    search_fields = ["flight_number", "airline", "origin", "destination"]
    date_hierarchy = "scheduled_time"
    inlines = [CrewAssignmentInline]


@admin.register(FlightAttendant)
class FlightAttendantAdmin(admin.ModelAdmin):
    list_display = ["full_name", "employee_id", "rank", "email", "roster_label"]
    list_filter = ["rank"]
    search_fields = ["first_name", "last_name", "employee_id"]


admin.site.register(Terminal)
admin.site.register(Gate)
admin.site.register(CrewAssignment)
