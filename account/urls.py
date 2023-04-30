from django.urls import path
from .views import Signup

urlpatterns = [
    path("signup/", Signup, name="signup") #http://localhost:8000/account/signup
]