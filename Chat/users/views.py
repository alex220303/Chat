from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import AddUserForm
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def register(request):
    if request.method == 'POST':
        form = AddUserForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        messages.success(request, f'Создан аккаунт {username}!')
        return redirect('blog-home')
    else:
        form = AddUserForm()
        return render(request, 'users/signup.html', {'form': form})