from django.urls import path, include
from .views import UserRegisterView
from django.contrib.auth import views
urlpatterns = [
path('register/', UserRegisterView.as_view(), name='register'),

]