from time import timezone
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    # redirects post detail when a post is created
    # reverse returns the full path as a string
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

        