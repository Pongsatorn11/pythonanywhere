from django.db import models


class SongType(models.Model):
    text = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.text}'

class Song(models.Model):
    songType = models.ForeignKey(SongType, on_delete = models.CASCADE)
    songName = models.CharField(max_length = 200)
    singer = models.CharField(max_length = 200)
    album = models.CharField(max_length = 200)

    def __str__(self):
        return f'{self.songType} - {self.songName} - {self.singer} - {self.album}'