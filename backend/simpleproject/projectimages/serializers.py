import base64
from django.core.files.base import ContentFile
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
# class SerializeImages(serializers.ModelSerializer):
#     image = serializers.CharField(write_only=True)
#     image_url = serializers.SerializerMethodField(read_only=True)
#
#     class Meta:
#         model = ModelImages
#         fields = ['id', 'image', 'description', 'image_url']
#
#     def get_image_url(self, obj):
#         if obj.image:
#             return obj.image.url
#         return None
#
#     def create(self, validated_data):
#         image_data = validated_data.pop('image')
#         format, imgstr = image_data.split(';base64,') if ';base64,' in image_data else ('', image_data)
#         ext = format.split('/')[-1] if format else 'jpg'
#         image = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)
#         model_instance = ModelImages.objects.create(image=image, **validated_data)
#         return model_instance