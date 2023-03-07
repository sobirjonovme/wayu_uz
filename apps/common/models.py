from django.db import models
from django.utils import timezone
from sorl.thumbnail import ImageField
from ckeditor_uploader.fields import RichTextUploadingField
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class PhoneNumberBaseModel(models.Model):
    phone_number = PhoneNumberField()

    class Meta:
        abstract = True


class PersonBaseModel(PhoneNumberBaseModel):
    image = ImageField(upload_to='images/')
    name = models.CharField(max_length=128)
    email = models.EmailField()
    position = models.CharField(max_length=128)
    bio = RichTextUploadingField()

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class TimeBaseModel(models.Model):
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True


class PostBaseModel(TimeBaseModel):
    image = ImageField(upload_to='images/')
    title = models.CharField(max_length=128)
    content = RichTextUploadingField()

    class Meta:
        abstract = True

    def __str__(self):
        return self.title
