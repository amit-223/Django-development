from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Emp(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=200)
    phone=models.CharField(max_length=10)
    working=models.BooleanField(default=True)
    # department=models.CharField(max_length=200)

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    message = models.CharField(max_length=200)
# def __str__(self):
#     return self.name

# class EmpTestimonial(models.Model):
#     # Your existing fields
#     picture = models.ImageField(upload_to='pictures/', null=True, blank=True)


class Testimonial(models.Model):
    name=models.CharField(max_length=200)
    testimonial=models.TextField()
    rating=models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=3)
  
    # picture=models.ImageField(upload_to='testimonial/')
    # picture = models.ImageField(upload_to='pictures/', null=True, blank=True)
    
    
