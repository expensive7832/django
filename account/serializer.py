from rest_framework import serializers
from .models import User

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', "username", "first_name", "last_name", "photo"]

class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()
    id = serializers.IntegerField(read_only=True)
    photo = serializers.CharField(read_only=True)

    def validate(self, data):
        user = User.objects.filter(email = data['email'], password = data['password']).first()

        if user is not None: 
            return user
        else:
            raise serializers.ValidationError("Invalid Credentials")
        

