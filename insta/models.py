from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Image(models.Model):
    image = models.ImageField(upload_to='photos/', blank=True, null=True)
    image_name = models.CharField(max_length=50)
    image_caption = models.TextField()
    profile = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    likes = models.IntegerField(default=0)
    comments = models.TextField(default=0)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.image_name


    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()
    
    def update_caption(self):
        self.save()

""" class Likes(models.Model):
    post_likes = models.ForeignKey(Image)

class Comments(models.Model):
    post_comments = models.ForeignKey(Image)
 """



class Profile(models.Model):
    user_name = models.ForeignKey(User,on_delete=models.CASCADE)
    profile =  models.ImageField(upload_to='profiles/', blank=True, null=True)
    bio = models.TextField()
