from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
	message = serializers.CharField(max_length=20) 