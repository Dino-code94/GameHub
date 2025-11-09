from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Registration page for new users
    path('register/', views.register, name='register'),

    # Login page - uses Django built-in login view
    path('login/', auth_views.LoginView.as_view(template_name='authapp/login.html', redirect_authenticated_user=True), name='login'),

    # Logout user and redirect home
    path('logout/', views.logout_view, name='logout'),
]
