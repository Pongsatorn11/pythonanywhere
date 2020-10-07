from django.contrib import admin

from .models import SongType, Song

admin.site.register(SongType)
admin.site.register(Song)