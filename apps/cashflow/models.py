from django.db import models

from apps.common.models import TimeBaseModel

PAYME = 'PYM'
OSON = 'OSN'
CLICK = 'CLK'

PAYMENT_TYPES = (
    (PAYME, 'payme'),
    (OSON, 'oson'),
    (CLICK, 'click'),
)


# Create your models here.
class Donation(TimeBaseModel):
    name = models.CharField(max_length=128)
    money_amount = models.DecimalField(max_digits=12, decimal_places=2)
    payment_type = models.CharField(max_length=3, choices=PAYMENT_TYPES)

    def __str__(self):
        return f"{self.name} | {self.money_amount}"


class Expense(TimeBaseModel):
    money_amount = models.DecimalField(max_digits=12, decimal_places=2)
    note = models.CharField(max_length=128)
    report = models.FileField(upload_to='reports/')

    def __str__(self):
        return f"{self.money_amount} | {self.note[:32]}..."
