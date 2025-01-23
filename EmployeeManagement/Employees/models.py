from django.db import models

# Create your models here.
class EmployeeData(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

