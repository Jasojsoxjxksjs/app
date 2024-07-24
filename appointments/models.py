from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    patient_name = models.CharField(max_length=100)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    case_type = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def duration(self):
        return (self.end_time - self.start_time).total_seconds() / 60  # in minutes

    def __str__(self):
        return f"{self.patient_name} - {self.case_type}"
