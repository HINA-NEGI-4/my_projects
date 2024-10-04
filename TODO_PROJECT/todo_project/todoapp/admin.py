from django.contrib import admin
from django.contrib.auth.models import User
from .models import TodoModel
# Register your models here.

class TodoAdmin(admin.ModelAdmin):
    list_display=['title','srno']

admin.site.register(TodoModel,TodoAdmin)    


   
