from django.db import models

# Create your models here.


from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    platforms = models.CharField(max_length=100)
    release_date = models.DateField()
    description = models.TextField()
    screenshot = models.ImageField(upload_to='screenshots/')
    video_url = models.URLField()
    rating = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    game = models.ForeignKey(Game, related_name='reviews', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review by {self.author.username} on {self.game.title}'
