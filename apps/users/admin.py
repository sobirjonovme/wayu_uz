from django.contrib import admin

from apps.users.models import CustomUser


# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    search_fields = ('username', 'first_name', 'last_name')
    list_display = ('id', 'username', 'first_name', 'last_name')


admin.site.register(CustomUser, CustomUserAdmin)

