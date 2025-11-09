from django.shortcuts import render, get_object_or_404
from .models import Game

def game_list(request):
    games = Game.objects.all()
    return render(request, 'games/index.html', {'games': games})

def game_detail(request, pk):
    game = get_object_or_404(Game, pk=pk)
    return render(request, 'games/detail.html', {'game': game})
