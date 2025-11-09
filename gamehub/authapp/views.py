from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout

def register(request):
    """
    Register a new user account.
    Creates a user, logs them in and redirects to homepage.
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        # Check password confirmation
        if password != password2:
            return render(request, 'authapp/register.html', {'error': 'Passwords do not match'})

        # Create user & login
        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect('/')

    # Show register page
    return render(request, 'authapp/register.html')


def logout_view(request):
    """
    Logout the current user and redirect to homepage.
    """
    logout(request)
    return redirect('/')
