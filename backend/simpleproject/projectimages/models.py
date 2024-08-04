from django.db import models


class ModelImages(models.Model):
    image = models.ImageField(upload_to='media/')
    description = models.TextField()

    def __str__(self):
        return self.image
