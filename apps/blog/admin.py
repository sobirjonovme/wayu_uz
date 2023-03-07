from django.contrib import admin

from apps.blog import models


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('name', )
    list_display = ('id', 'name')


class TagAdmin(admin.ModelAdmin):
    search_fields = ('name', )
    list_display = ('id', 'name')


class NewsAdmin(admin.ModelAdmin):
    search_fields = ('title', )
    list_display = ('id', 'title', 'category')


class NewsTagAdmin(admin.ModelAdmin):
    search_fields = ('news__title', 'tag__name')
    list_display = ('id', 'news', 'tag')


class EventAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ('id', 'title', 'type', 'address')


class BookAdmin(admin.ModelAdmin):
    search_fields = ('title', 'author')
    list_display = ('id', 'title', 'author', 'language')


admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Tag, TagAdmin)
admin.site.register(models.News, NewsAdmin)
admin.site.register(models.NewsTag, NewsTagAdmin)
admin.site.register(models.Event, EventAdmin)
admin.site.register(models.Book, BookAdmin)
