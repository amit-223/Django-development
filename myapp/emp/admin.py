from django.contrib import admin
from .models import Emp,Testimonial

# Register your models here.


class Empadmin(admin.ModelAdmin):
    list_display=('name','id','phone')
    search_fields=('name','phone')

admin.site.register(Emp, Empadmin)
admin.site.register(Testimonial)