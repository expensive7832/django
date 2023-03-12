from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User
from .serializer import userSerializer, LoginSerializer
# Create your views here.



@api_view(['POST'])
def Register(request):
    

    serializer = userSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

       

        return Response(data={"message": "user account created"})
    else:
        
        return Response(data=serializer.errors)

@api_view(['POST'])
def Login(request):

    data = request.data

    serializer = LoginSerializer(data=data)

    if serializer.is_valid():
        return Response(data={"info": serializer.data, "message": "login successful"})
    else:
        return Response(data={"info": serializer.errors, "message":"error"})
    

@api_view(['GET'])
def getUsers(request):

    users = User.objects.all()
    
    serializer = userSerializer(users, many=True)

    return Response(data=serializer.data)