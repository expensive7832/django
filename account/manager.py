from django.contrib.auth.base_user import BaseUserManager

class customizeUser(BaseUserManager):

    def create_user(self, email, password, **extra_data):

        if not email:
            raise ValueError("Email Must be Specify")

        email = self.normalize_email(email)

        user = self.model(email = email, **extra_data)
        user.set_password(password)
        user.save()

        return user
    
    def create_superuser(self, email, password, **extra_data):
        extra_data.setdefault('is_active', True)
        extra_data.setdefault('is_staff', True)
        extra_data.setdefault('is_superuser', True)

        if extra_data.get('is_staff') is not True:
            raise ValueError("User Must Be Staff")
        
        if extra_data.get('is_active') is not True:
            raise ValueError("User Must Be Active")
        
        if extra_data.get('is_superuser') is not True:
            raise ValueError("User Must Be Admin")
        
        return self.create_superuser(email=email, password=password, **extra_data)

