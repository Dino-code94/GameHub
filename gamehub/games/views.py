from django.shortcuts import render, get_object_or_404, redirect
from .models import Game, Comment

def game_list(request):
    games = Game.objects.all()
    return render(request, 'games/index.html', {'games': games})

def game_detail(request, pk):
    game = get_object_or_404(Game, pk=pk)

    if request.method == 'POST':
        text = request.POST.get('text')
        if text and request.user.is_authenticated:
            Comment.objects.create(game=game, user=request.user, text=text)
            return redirect('game_detail', pk=pk)

    comments = game.comments.all()

    return render(request, 'games/detail.html', {'game': game, 'comments': comments})
