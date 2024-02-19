from django.shortcuts import render

def base(request):
    is_auth = False
    dialogs = 0
    return render(request, 'chat.html', context={'is_auth': is_auth,
                                                 'dialogs': dialogs})

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')
