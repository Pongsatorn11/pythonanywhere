from django.forms import ModelForm
from django import forms

from .models import Song , Link

class addLink(ModelForm):
    class Meta:
        model = Link
        fields = ['Link_a']


class addSong(ModelForm):
    class Meta:
        model = Song
        fields = ['Song_Name','Link','Singer']