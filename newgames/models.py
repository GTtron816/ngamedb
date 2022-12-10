from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings
class Game(models.Model):
    title = models.CharField(max_length=255)
    dev=models.CharField(max_length=255)
    pub=models.CharField(max_length=255)
    gen=models.CharField(max_length=255)
    gtype=models.CharField(max_length=255)
    syn=models.TextField()
    title_img = models.ImageField(null=True, blank=True, upload_to="title_imgs")
    sc1 = models.ImageField(null=True, blank=True, upload_to="screenshots")
    sc2 = models.ImageField(null=True, blank=True, upload_to="screenshots")
    sc3 = models.ImageField(null=True, blank=True, upload_to="screenshots")
    trailer=models.CharField(max_length=255,null=True,blank=True)
    plat=models.CharField(max_length=255,null=True,blank=True)
    hype = models.ManyToManyField(User, related_name='new_games')
    meh = models.ManyToManyField(User, related_name='mehed')
    def total_hype(self):
        return self.hype.count()

    def total_mehs(self):
        return self.meh.count()

 
    def __str__(self):
        return self.title + '|' + self.dev + '|' + self.pub
    
    def get_absolute_url(self):
        return reverse('gamedetails', args=(str(self.id)))


class Comment(models.Model):
    game = models.ForeignKey(Game,related_name="comments",on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField()
    date_added = models. DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.game.title, self.name)
    
   
    
   
