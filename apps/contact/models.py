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


class CommonQuestion(TimeBaseModel):
    question = models.CharField(max_length=256)
    answer = models.TextField()


class Vacancy(TimeBaseModel, PhoneNumberBaseModel):
    title = models.CharField(max_length=150)
    salary = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    status = models.CharField(max_length=3, choices=VACANCY_STATUS)


class Application(TimeBaseModel, PhoneNumberBaseModel):
    name = models.CharField(max_length=128, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    type = models.CharField(max_length=3, choices=APPLICATION_TYPES)
    resume = models.FileField(upload_to='resumes/')
