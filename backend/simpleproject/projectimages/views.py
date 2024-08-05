from rest_framework import viewsets
from .models import ModelImages
from .serializers import ImageModelSerializer


class ViewSetImages(viewsets.ModelViewSet):
    queryset = ModelImages.objects.all()
    serializer_class = ImageModelSerializer

