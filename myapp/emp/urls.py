from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
  path('home/',empfunc),
  path('add-emp/', add_emp),
  path("testimonials/",testimonials),
  path("feedback/",feedback),
]