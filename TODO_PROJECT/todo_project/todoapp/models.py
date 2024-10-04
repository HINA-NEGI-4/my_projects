from django.db import models
from django.contrib.auth.models import User,AbstractUser,Group,Permission
from django.contrib import auth
# Create your models here.

class UserModel(AbstractUser):
    email=models.EmailField(unique=True)
    username = models.CharField(max_length=20, unique=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS=[]

    groups= models.ManyToManyField(
        Group,
        related_name='custom_user_groups',
        blank=True

    )

    user_permissions =models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions',
        blank=True
    )

class TodoModel(models.Model):
    title=models.CharField(max_length=50)
    srno=models.AutoField(primary_key=True,auto_created=True)
    date=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
      
   