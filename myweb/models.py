from django.db import models

class Singer(models.Model):

    id = models.AutoField(primary_key=True)

    Singer = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.Singer}'


class Link(models.Model):
    id = models.AutoField(primary_key=True)
    Link_a = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.Link_a}'


class Song(models.Model):
    Song_Name = models.CharField(max_length=100)

    Singer = models.ForeignKey(Singer, on_delete=models.CASCADE)
    Link = models.ForeignKey(Link, on_delete=models.CASCADE)

    def __str__(self):

        return f'{self.Song_Name} - {self.Link} - {self.Singer}'