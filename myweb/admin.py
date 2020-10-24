from django.contrib import admin

from .models import Singer, Song, Link

admin.site.register(Singer)
admin.site.register(Song)
admin.site.register(Link)