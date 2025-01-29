from django.contrib import admin
from .models import Emp,Testimonial, Feedback

# Register your models here.


class Empadmin(admin.ModelAdmin):
    list_display=('name','id','phone')
    search_fields=('name','phone')

class Feedbackadmin(admin.ModelAdmin):
    list_display=('name', 'message')

admin.site.register(Emp, Empadmin)
admin.site.register(Testimonial)
admin.site.register(Feedback, Feedbackadmin)