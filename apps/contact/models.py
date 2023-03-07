from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

from apps.common.models import TimeBaseModel, PhoneNumberBaseModel


VACANCY = 'VAC'
VOLUNTEER = 'VOL'

ACTIVE = 'ACT'
END = 'END'

APPLICATION_TYPES = (
    (VACANCY, 'vacancy'),
    (VOLUNTEER, 'volunteer'),
)

VACANCY_STATUS = (
    (ACTIVE, 'active'),
    (END, 'end')
)


# Create your models here.
class Message(TimeBaseModel, PhoneNumberBaseModel):
    name = models.CharField(max_length=128)
    content = models.TextField()

    def __str__(self):
        return f"by {self.name} | {self.content[:30]}..."


class CommonQuestion(TimeBaseModel):
    question = models.CharField(max_length=256)
    answer = models.TextField()

    def __str__(self):
        return f"{self.question[:30]}..."


class Vacancy(TimeBaseModel, PhoneNumberBaseModel):
    title = models.CharField(max_length=150)
    salary = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    content = RichTextUploadingField()
    status = models.CharField(max_length=3, choices=VACANCY_STATUS)

    def __str__(self):
        return self.title


class Application(TimeBaseModel, PhoneNumberBaseModel):
    name = models.CharField(max_length=128, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    vacancy = models.ForeignKey(
        Vacancy, on_delete=models.CASCADE, related_name='applications',
        null=True, blank=True
    )
    type = models.CharField(max_length=3, choices=APPLICATION_TYPES)
    resume = models.FileField(upload_to='resumes/')

    def __str__(self):
        return f"{self.name} | {self.vacancy}"
