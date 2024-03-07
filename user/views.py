from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth.forms import UserCreationForm
from . import templates



def registerView(request):
    if request.method == 'POST':
        
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirmPassword = request.POST['confirmPassword']
        if password==confirmPassword:
         if User.objects.filter(email==email).exists():
            print('Email already exists')
         else:
            user = User.objects.create_user(first_name=first_name,last_name=last_name,email=email,password=password,confirmPassword=confirmPassword)
            user.save()
            return user
        print('User created')
            # return redirect('/')
    else:
     print('User not created')
     return render(request,'registerUser.html')

def loginView(request):
   if request.method=='POST':
      email = request.POST['email']
      password = request.POST['password'] 
      user = auth.authenticate(email=email,password=password)
      if user is not None:
         auth.login(request,user)
         return redirect('/')
      else:
         messages.info(request,'Invalid credentials')
         return redirect('login/')
         
   else:   
        return render(request,'loginUser.html')
    
def regView(request):
      return render(request,'register.html')