from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
  path('home/',empfunc),
  path('add-emp/', add_emp),
  path('delete-emp/<int:e_id>',del_emp),
  path("testimonials/",testimonials),
  path("feedback/",feedback),
  path('update-emp/<int:e_id>',update_emp)
]