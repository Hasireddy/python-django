from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from . import templates



def registerView(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        confirmPassword = request.POST['confirmPassword']
        if password==confirmPassword:
         if User.objects.filter(email==email).exists():
            print('Email already exists')
         else:
            user = User.objects.create_user(firstname=firstname,lastname=lastname,email=email,password=password,confirmPassword=confirmPassword)
            user.save()
            return user
            print('User created')
            # return redirect('/')
    else:
     print('User not created')
     return render(request,'registerUser.html')

def loginView(request):
   return render(request,'loginUser.html')
    
   