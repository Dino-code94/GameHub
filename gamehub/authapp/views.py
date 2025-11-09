from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password != password2:
            return render(request, 'authapp/register.html', {'error':'Passwords do not match'})

        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect('/')

    return render(request, 'authapp/register.html')

def logout_view(request):
    logout(request)
    return redirect('/')
