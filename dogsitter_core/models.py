from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, models.CASCADE)
    location = models.CharField(max_length=1000)
    cost = models.DecimalField(decimal_places=2, max_digits=7)
    is_dog_sitter = models.BooleanField(default=False)
    bio = models.TextField(max_length=1000000)

    def __str__(self):
        return str(self.user)


class MultipleImages(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    images = models.FileField(upload_to='files')