from django.contrib import admin
from .models import Emp,Testimonial, Feedback

class Empadmin(admin.ModelAdmin):
    list_display=('name','id','phone')
    search_fields=('name','phone')

class Feedbackadmin(admin.ModelAdmin):
    list_display=('name', 'message')
    
class TestiAdmin(admin.ModelAdmin):
    list_display=('name', 'testimonial', 'rating')

admin.site.register(Emp, Empadmin)
admin.site.register(Testimonial, TestiAdmin)
admin.site.register(Feedback, Feedbackadmin)