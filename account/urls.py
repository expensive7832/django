from django.urls import path
from .views import Register, Login, getUsers
urlpatterns = [
    path("signup/", Register ),
    path("login/", Login),
    path("allusers/", getUsers),
]