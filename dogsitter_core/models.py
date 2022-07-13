from django.db import models
from django.contrib.auth.models import User
from datetime import date



class Profile(models.Model):
    user = models.OneToOneField(User, models.CASCADE)
    location = models.CharField(max_length=1000)
    cost = models.DecimalField(decimal_places=2, max_digits=7)
    is_dog_sitter = models.BooleanField(default=False)
    bio = models.TextField(max_length=1000000)

    def __str__(self):
        return str(self.user)


class Dog(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    name = models.CharField(max_length=200)
    weight = models.DecimalField(decimal_places=2, max_digits=7)
    good_with_cats = models.BooleanField(default=False)
    good_with_kids = models.BooleanField(default=False)
    good_with_dogs = models.BooleanField(default=False)
    bio = models.TextField(max_length=100000)
    dob = models.DateField()

    def __str__(self):
        return str(self.name)
