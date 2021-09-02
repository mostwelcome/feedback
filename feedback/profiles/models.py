from django.db import models


class UserProfile(models.Model):
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.image
