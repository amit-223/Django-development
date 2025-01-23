from django.urls import path
from .views import LoginAPIView,login_page

urlpatterns = [
    # path('login/', LoginAPIView.as_view(), name='login'),
    path('login/', login_page, name='login_page'),  # Render login page
    path('api/login/', LoginAPIView.as_view(), name='login'),  # API for login
]
