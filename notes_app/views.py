from django.shortcuts import render
from django.contrib.auth import authenticate, login 
from django.contrib.auth.models import User


def sign_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username =username, password = password )

        if user is not None:
            login(request, user)
            return render(request,'index.html' )

    
    return render (request, 'auth-sign-in.html')

def register(request):
    if request.method == 'POST':
        user= User.objects.create(username = request.POST['username'])
        user.set_password(request.POST['password'])
        user.save()
        return render(request,'success.html' )


    return render(request,'auth-sign-up.html')

def success(request):
    return render(request, 'success.html')