from django.urls import path
from . import views

urlpatterns = [
    # Homepage - list of all games
    path('', views.game_list, name='game_list'),

    # Individual game detail page (pk = primary key)
    path('game/<int:pk>/', views.game_detail, name='game_detail'),
]
