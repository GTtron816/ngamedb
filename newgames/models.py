from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):
    title = models.CharField(max_length=255)
    dev=models.CharField(max_length=255)
    pub=models.CharField(max_length=255)
    gen=models.CharField(max_length=255)
    gtype=models.CharField(max_length=255)
    syn=models.TextField()

    def __str__(self):
        return self.title + '|' + self.dev + '|' + self.pub



