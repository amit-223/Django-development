from django.db import models

# Create your models here.
# models pe apan data rakenge aur, data ko database mai dalenge
class Students(models.Model):
    name=models.CharField(max_length=200)
    college=models.CharField(max_length=200)
    id=models.IntegerField(primary_key=True)
    isactive=models.BooleanField(default=False)