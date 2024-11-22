from django.contrib.auth.models import User
from django.db import models

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100)
    experience_years = models.IntegerField()
    availability = models.JSONField()  # Store available times

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    medical_history = models.TextField(blank=True, null=True)

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    symptoms = models.TextField()
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Complete', 'Complete')])
