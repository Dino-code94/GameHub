from django.db import models

class Game(models.Model):
    title = models.CharField(max_length=120)
    cover = models.ImageField(upload_to='covers/')
    description = models.TextField()

    def __str__(self):
        return self.title
