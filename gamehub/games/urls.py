from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name='home'),
    path('game/<int:pk>/', views.game_detail, name='game_detail'),

]
