from django.contrib import admin
from . import models

@admin.register(models.Post)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', 'id','status', 'author')

admin.site.register(models.Album)
admin.site.register(models.Genre)
admin.site.register(models.Artist)
admin.site.register(models.Song)
