from django.db import models

class Donor(models.Model):
    name = models.CharField(max_length=100)
    blood_group = models.CharField(max_length=5)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10)

class BloodRequest(models.Model):
    patient_name = models.CharField(max_length=100)
    blood_group = models.CharField(max_length=5)
    location = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    patient_condition = models.TextField()

    def __str__(self):
        return self.patient_name
