from django.db import models

class Game(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    cover = models.ImageField(upload_to='covers/', null=True, blank=True)

    def __str__(self):
        return self.title
