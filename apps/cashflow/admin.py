from django.contrib import admin

from apps.cashflow import models


# Register your models here.
class DonationAdmin(admin.ModelAdmin):
    search_fields = ('name', 'tag__name')
    list_display = ('id', 'name', 'money_amount', 'payment_type')


class ExpenseAdmin(admin.ModelAdmin):
    search_fields = ('name', 'tag__name')
    list_display = ('id', 'money_amount', 'note')


admin.site.register(models.Donation, DonationAdmin)
admin.site.register(models.Expense, ExpenseAdmin)
