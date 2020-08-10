from django.db import models

# Create your models here.

class Image(models.Model):
    image = models.ImageField(upload_to='photos/', blank=True, null=True)
    image_name = models.CharField(max_length=50)
    image_caption = models.TextField()
    profile = models.ForeignKey(Profile)
    likes = models.IntegerField()
    comments = models.TextField()

    def __str__(self):
        return self.image_name


    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()






