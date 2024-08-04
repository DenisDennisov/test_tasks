from django.urls import path, include
from rest_framework import routers
from .views import ViewSetImages

router = routers.DefaultRouter()
router.register(r'projectimages', ViewSetImages)

urlpatterns = [
    path(r'', include(router.urls)),
]
