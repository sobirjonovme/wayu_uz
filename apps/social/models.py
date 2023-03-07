from django.db import models
from sorl.thumbnail import ImageField

from apps.common.models import TimeBaseModel


# Create your models here.
class InstagramPost(TimeBaseModel):
    image = ImageField(upload_to='instagram/')
    link = models.URLField()

    def __str__(self):
        return f"{self.id} | {self.link}"


class UsefulLink(InstagramPost):
    description = models.CharField(max_length=100)
