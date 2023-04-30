from django.http import HttpResponse


def Signup(request):
    return HttpResponse("guess you want to signup")

def Login(request):
    return HttpResponse("guess you want to login")