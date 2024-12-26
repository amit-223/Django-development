from django.db import models

# Create your models here.
class Emp(models.Model):
    name=models.CharField(max_length=200)
    empid=models.CharField(max_length=200)
    phone=models.CharField(max_length=10,null=False, blank=False)
    working=models.BooleanField(default=True)
    department=models.CharField(max_length=200)

def __str__(self):
    return self.name

# class EmpTestimonial(models.Model):
#     # Your existing fields
#     picture = models.ImageField(upload_to='pictures/', null=True, blank=True)


class Testimonial(models.Model):
    name=models.CharField(max_length=200)
    testimonial=models.TextField()
    # picture=models.ImageField(upload_to='testimonial/')
    picture = models.ImageField(upload_to='pictures/', null=True, blank=True)
    # rating=models.IntegerField()
    def __str__(self):
        return self.testimonial
    
