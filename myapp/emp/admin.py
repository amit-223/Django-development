from django.contrib import admin
from .models import Emp,Testimonial

# Register your models here.


class Empadmin(admin.ModelAdmin):
    list_display=('name','working','id','phone')
    search_fields=('name','phone')
    list_filter=('working',)

admin.site.register(Emp, Empadmin)
admin.site.register(Testimonial)