from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.



@api_view(['POST'])
def Register(request):
    return Response(data=request.data)

def Login(request):
    return Response(data="login in....")