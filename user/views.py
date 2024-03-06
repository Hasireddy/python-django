from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from . import templates



def registerView(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        # user = User.objects.create_user(first_name=first_name,last_name=last_name,email=email,password=password)
        # user.save()
        # return user
        print('User created')
        # return redirect('/')
    else:
     return render(request,'registerUser.html')
