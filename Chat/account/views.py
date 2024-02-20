from django.shortcuts import render
from .forms import *

def login(request):
    form = AddUserForm()
    if request.method == 'POST':
        return render(request, 'chat.html')
    return render(request, 'login.html', context={'form' : form, 'title' : 'Sign in'})

def signup(request):
    return render(request, 'signup.html')

def logout(request):
    return render(request, 'signup.html')
