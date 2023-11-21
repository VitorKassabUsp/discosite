from django.db import models
from django.conf import settings
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField(default="")
    post_date = models.DateTimeField(default=timezone.now)
    
    band = models.CharField(max_length=30)
    release_year = models.IntegerField()
    poster_url = models.URLField(max_length=200, null=True)

    def __str__(self):
        return f'{self.title} ({self.release_year})'
    



