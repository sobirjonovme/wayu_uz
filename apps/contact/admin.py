from django.contrib import admin

from apps.contact import models


# Register your models here.
class MessageAdmin(admin.ModelAdmin):
    search_fields = ('name', )
    list_display = ('id', 'name', 'phone_number', 'created_at')


class CommonQuestionAdmin(admin.ModelAdmin):
    search_fields = ('question', )
    list_display = ('id', 'question')


class VacancyAdmin(admin.ModelAdmin):
    search_fields = ('title', )
    list_display = ('id', 'title', 'salary', 'status')


class ApplicationAdmin(admin.ModelAdmin):
    search_fields = ('name', )
    list_display = ('id', 'name', 'type')


admin.site.register(models.Message, MessageAdmin)
admin.site.register(models.CommonQuestion, CommonQuestionAdmin)
admin.site.register(models.Vacancy, VacancyAdmin)
admin.site.register(models.Application, ApplicationAdmin)



