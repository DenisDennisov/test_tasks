from django.db import models


class ModelImages(models.Model):
    image = models.TextField()
    description = models.TextField(max_length=4000)

    def __str__(self):
        return self.image
