from django.shortcuts import render


def sign_in(request):
    return render (request, 'auth-sign-in.html')