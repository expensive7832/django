from django.urls import path
from .views import Register, Login
urlpatterns = [
    path("signup/", Register ),
    path("login/", Login)
]