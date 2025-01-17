from typing import Any
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.base_user import AbstractBaseUser
from django.http import HttpRequest

class EmailBackend(ModelBackend):
    def authenticate(self, request, email=None,password=None,**kwargs):
        UserModel=get_user_model()
        try:
            user=UserModel.objects.get(email=email)
            if user.check_password(password):
                return user
        except UserModel.DoesNotExist:
            print('exception')
            return None    
