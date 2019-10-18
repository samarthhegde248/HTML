from .models import music_library
from rest_framework import serializers


class music_librarySerializer(serializers.ModelSerializer):
    class Meta:
        model = music_library
        fields = ['songName', 'artist', 'genre']