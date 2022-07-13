from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



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
    weight = models.IntegerField()
    good_with_cats = models.BooleanField(default=False)
    good_with_kids = models.BooleanField(default=False)
    good_with_dogs = models.BooleanField(default=False)
    bio = models.TextField(max_length=100000)
    dob = models.DateField()

    def __str__(self):
        return str(self.name)

    def age(self):
        time_lived = timezone.now().date() - self.dob
        months_lived = time_lived.days//30.5
        if months_lived <1:
            return f'{time_lived.days} days'
        if months_lived < 12:
            return f'{int(months_lived)} months'
        elif months_lived < 24:
            return f'{int(months_lived//12)} years and {int(months_lived%12)} months'
        else:
            return f'{int(months_lived)//12} years'
