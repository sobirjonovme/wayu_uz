from django.contrib import admin

from apps.social import models


# Register your models here.
class InstagramPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'link')


admin.site.register(models.InstagramPost, InstagramPostAdmin)
admin.site.register(models.UsefulLink, InstagramPostAdmin)
