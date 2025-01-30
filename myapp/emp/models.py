from django.db import models

class Emp(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=200)
    phone=models.CharField(max_length=10)
    working=models.BooleanField(default=True)

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    message = models.CharField(max_length=200)

class Testimonial(models.Model):
    name=models.CharField(max_length=200)
    testimonial=models.TextField()
    rating=models.CharField(max_length=10)
  
   
    
    
