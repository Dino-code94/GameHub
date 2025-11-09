from django.shortcuts import render, get_object_or_404, redirect
from .models import Game, Comment

def game_list(request):
    """
    Display list of all games.
    Homepage game catalog.
    """
    games = Game.objects.all()  # get all games
    return render(request, 'games/index.html', {'games': games})


def game_detail(request, pk):
    """
    Display detail page for a single game.
    Also handles creating a comment for this game.
    """
    game = get_object_or_404(Game, pk=pk)  # get selected game or 404

    # Handle comment submit
    if request.method == 'POST':
        text = request.POST.get('text')

        # Only allow logged-in users to comment
        if text and request.user.is_authenticated:
            Comment.objects.create(
                game=game,
                user=request.user,
                text=text
            )
            return redirect('game_detail', pk=pk)

    # Get all comments for this game
    comments = game.comments.all()

    # Render detail page
    return render(request, 'games/detail.html', {'game': game, 'comments': comments})
