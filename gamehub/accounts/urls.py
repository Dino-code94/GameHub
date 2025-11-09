from django.urls import path
from . import views

urlpatterns = [
    # Custom login view (if used instead of Django built-in auth)
    path('login/', views.login_view, name='login'),
]
