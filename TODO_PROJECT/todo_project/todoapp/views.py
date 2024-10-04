from django.shortcuts import render,render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password,check_password
from django.views.generic import ListView
from django.contrib.auth import authenticate,login
from django.contrib import messages
from .models import TodoModel
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def signup_view(request):
    if request.method=='POST':
        username=request.POST.get('name')
        password=request.POST.get('password')
        email=request.POST.get('email')
        if User.objects.filter(email=email).exists():
            error_msg = {'error_msg': 'This email already exists. Please sign up with another email.'}
            return render(request, 'todoapp/signup.html', error_msg)
        user_object=User(username=username,email=email)
        user_object.set_password(password)
        user_object.save()
        return redirect('login')
           

    return render(request,'todoapp/signup.html')

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        user=authenticate(request,email=email,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:  
            return render(request,'todoapp/login.html')
    return render(request,'todoapp/login.html')      

@login_required
def home_view(request):
    if request.method=='POST':
        if request.user.is_authenticated:
            title=request.POST.get('title')
            task=TodoModel(title=title,user=request.user)
            task.save()
            messages.success(request,'added succesfully')
            return render(request,'todoapp/home.html')
    return render(request,'todoapp/home.html')

@login_required
def user_data(request):
    task=TodoModel.objects.filter(user=request.user)
    return render(request,'todoapp/todo_list.html',{'task':task}) 


@login_required     
def delete_view(request,id):
    user_data=TodoModel.objects.filter(srno=id)
    user_data.delete()
    return redirect('todolist')  

@login_required  
def update_view(request,id):
    user_data=get_object_or_404(TodoModel,srno=id)
    if request.method=='POST':
        user=request.user
        task=request.POST.get('title')
        user_data.title=task
        user_data.user=user
        user_data.save()
        return redirect('home')
    print(user_data.title)
    return render(request,'todoapp/home.html',{'user_data':user_data})    
def logout_view(request):
    logout(request)
    redirect('login') 