from rest_framework import serializers
from .models import ModelImages


class ImageModelSerializer(serializers.ModelSerializer):
    image = serializers.CharField(required=False)

    class Meta:
        model = ModelImages
        fields = ['id', 'image', 'description']

    def create(self, validated_data):
        image_data = validated_data.pop('image', None)
        if image_data:
            validated_data['image'] = image_data
        return super().create(validated_data)

    def update(self, instance, validated_data):
        image_data = validated_data.pop('image', None)
        if image_data:
            instance.image = image_data
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance
