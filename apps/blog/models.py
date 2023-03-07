from django.db import models

from apps.common.models import PostBaseModel


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class News(PostBaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='news')


class NewsTag(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='tags')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='news')

    def __str__(self):
        return f"{self.news.title} | {self.tag.name}"


class Event(PostBaseModel):
    type = models.CharField(max_length=64)
    scheduled_at = models.DateTimeField()
    address = models.CharField(max_length=100)


class Book(PostBaseModel):
    author = models.CharField(max_length=128)
    language = models.CharField(max_length=64)
    file = models.FileField(upload_to='files/')
