from rest_framework import serializers
from .models import ModelImages


class SerializeImages(serializers.ModelSerializer):
    class Meta:
        model = ModelImages
        fields = ['id', 'image', 'description']
