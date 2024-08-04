from rest_framework import viewsets
from .models import ModelImages
from .serializers import SerializeImages


class ViewSetImages(viewsets.ModelViewSet):
    queryset = ModelImages.objects.all()
    serializer_class = SerializeImages
