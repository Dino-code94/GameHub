from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):
    """
    Represents a single game in the database.
    """
    title = models.CharField(max_length=200)
    description = models.TextField()
    cover = models.ImageField(upload_to='covers/', null=True, blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    """
    Represents a comment left by a user on a specific game.
    """
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.game.title}"
