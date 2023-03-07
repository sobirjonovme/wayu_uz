from django.contrib import admin

from apps.about import models


# Register your models here.
class ChairmanAdmin(admin.ModelAdmin):
    search_fields = ('name', )
    list_display = ('id', 'name', 'position', 'year')


class ManagerAdmin(admin.ModelAdmin):
    search_fields = ('name', )
    list_display = ('id', 'name', 'position', 'reception_day')


class BranchAdmin(admin.ModelAdmin):
    search_fields = ('country', 'city')
    list_display = ('id', 'country', 'city')


class RepresentativeAdmin(admin.ModelAdmin):
    search_fields = ('name', )
    list_display = ('id', 'name', 'branch')


class SponsorAdmin(admin.ModelAdmin):
    search_fields = ('name', )
    list_display = ('id', 'name', 'link')


admin.site.register(models.Chairman, ChairmanAdmin)
admin.site.register(models.Manager, ManagerAdmin)
admin.site.register(models.Branch, BranchAdmin)
admin.site.register(models.Representative, RepresentativeAdmin)
admin.site.register(models.Sponsor, SponsorAdmin)
