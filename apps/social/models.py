from django.db import models
from sorl.thumbnail import ImageField


# Create your models here.
class InstagramPost(models.Model):
    image = ImageField(upload_to='instagram/')
    link = models.URLField()


class UsefulLink(InstagramPost):
    description = models.CharField(max_length=100)
