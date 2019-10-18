from rest_framework import serializers
from .models import musicLibrary

class MusicLibrarySerializers(serializers.Serializer):
    songName = serializers.CharField(max_length = 50)
    artist = serializers.CharField(max_length = 50)
    genre =serializers.CharField(max_length = 20)

    def create(self, validated_data):
        return musicLibrary.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.songName = validated_data.get('songName', instance.songName)
        instance.artist = validated_data.get('artist', instance.artist)
        instance.genre = validated_data('genre', instance.genre)

        instance.save()
        return instance
