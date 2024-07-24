from django.contrib import admin
from .models import Doctor, Appointment


# Register your models here.
@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient_name', 'doctor', 'case_type', 'start_time', 'end_time', 'cost', 'duration')
