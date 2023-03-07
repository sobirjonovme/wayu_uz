from django.db import models
from sorl.thumbnail import ImageField

from apps.common.models import PersonBaseModel


# Create your models here.
class Chairman(PersonBaseModel):
    year = models.IntegerField()


class Manager(PersonBaseModel):
    reception_day = models.CharField(max_length=256)


class Branch(models.Model):
    country = models.CharField(max_length=128)
    flag = ImageField(upload_to='flags/')
    city = models.CharField(max_length=128)
    lat = models.FloatField()
    long = models.FloatField()

    def __str__(self):
        return f"{self.country} | {self.city}"


class Representative(PersonBaseModel):
    branch = models.OneToOneField(
        Branch,
        on_delete=models.CASCADE
    )


class Sponsor(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=64)
    image = ImageField(upload_to='images/')
    link = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name
