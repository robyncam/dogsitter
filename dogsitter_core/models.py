from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import date
from multiselectfield import MultiSelectField


class Profile(models.Model):
    user = models.OneToOneField(User, models.CASCADE)
    location = models.CharField(max_length=1000)
    bio = models.TextField(max_length=1000000)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return str(self.user)


class DogSitterProfile(models.Model):
    ALONE = 'alone'
    WITH_SPOUSE = 'with_spouse'
    WITH_ROOMMATES = 'with_roommates'
    WITH_SPOUSE_CHILDREN = 'with_spouse_and_children'
    WITH_CHILDREN = 'with_children'

    LIVING_ARRANGEMENTS = [
        (ALONE, 'I live alone'),
        (WITH_SPOUSE, 'I live with my spouse/partner'),
        (WITH_ROOMMATES, 'I live with roommates'),
        (WITH_SPOUSE_CHILDREN, 'I live with my spouse and children'),
        (WITH_CHILDREN, 'I live with children')
    ]

    HOUSE = 'house'
    APARTMENT = 'apartment'
    CONDO = 'condo'
    ALTERNATIVE = 'alternative'

    HOUSE_CHOICES = [
        (HOUSE, 'I live in a house'),
        (APARTMENT, 'I live in an apartment'),
        (CONDO, 'I live in a condo'),
        (ALTERNATIVE, 'I live in an alternative style of housing'),
    ]

    SMALL = "small"
    MEDIUM = "medium"
    LARGE = "large"
    EXTRA_LARGE = "extra_large"

    DOG_SIZES = [
        (SMALL, "Small Dogs (up to 22lbs)"),
        (MEDIUM, "Medium Dogs (23lbs to 55lbs)"),
        (LARGE, "Large Dogs (up to 100lbs)"),
        (EXTRA_LARGE, "Extra Large Dogs (over 100lbs)"),
    ]

    ZERO_ = 'zero'
    UP_TO_TWO = 'two_hours'
    UP_TO_FOUR = 'four_hours'
    UP_TO_EIGHT = 'eight_hours'

    HOURS_CHOICES = [
        (ZERO_, 'Your dog will not be left alone'),
        (UP_TO_TWO, 'Up to two hours'),
        (UP_TO_FOUR, 'Up to four hours'),
        (UP_TO_EIGHT, 'Up to eight hours'),
    ]

    ONE = 'one'
    TWO = 'two'
    TWO_PLUS = 'more than two'

    WALK_CHOICES = [
        (ONE, 'One'),
        (TWO, 'Two'),
        (TWO_PLUS, 'More than two'),
    ]

    DOGBED = 'dogbed'
    BED = 'bed'
    COUCH = 'couch'
    ANYWHERE = 'anywhere'

    SLEEPING_CHOICES = [
        (DOGBED, 'On a dogbed'),
        (BED, 'On the bed'),
        (COUCH, 'On the couch'),
        (ANYWHERE, 'Wherever they would like'),
    ]

    user = models.OneToOneField(User, models.CASCADE)
    living_arrangements = models.CharField(max_length=1000,
                                           choices=LIVING_ARRANGEMENTS, default="")
    housing = models.CharField(max_length=1000, choices=HOUSE_CHOICES, default="")
    yard = models.BooleanField(default=False)
    cost = models.DecimalField(decimal_places=2, max_digits=7)
    dog_sizes = MultiSelectField(choices=DOG_SIZES, default='')
    hours_alone = models.CharField(max_length=1000, choices=HOURS_CHOICES, default="")
    walks = models.CharField(max_length=1000, choices=WALK_CHOICES, default="")
    sleeping_arrangements = models.CharField(max_length=1000, choices=SLEEPING_CHOICES, default="")


class Dog(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    name = models.CharField(max_length=200)
    weight = models.IntegerField()
    good_with_cats = models.BooleanField(default=False)
    good_with_kids = models.BooleanField(default=False)
    good_with_dogs = models.BooleanField(default=False)
    bio = models.TextField(max_length=100000)
    dob = models.DateField()
    breed = models.CharField(max_length=1000)
    image = models.ImageField(default='DogProfile.png', upload_to='dog_pics')

    def __str__(self):
        return str(self.name)

    def age(self):
        time_lived = timezone.now().date() - self.dob
        months_lived = time_lived.days//30.5
        if months_lived < 1:
            return f'{time_lived.days} days'
        if months_lived < 12:
            return f'{int(months_lived)} months'
        elif months_lived < 24:
            return f'{int(months_lived//12)} years and {int(months_lived%12)} months'
        else:
            return f'{int(months_lived)//12} years'

    def is_birthday_today(self):
        date_today = date.today()
        day = date_today.day
        month = date_today.month
        birth_day = self.dob.day
        birth_month = self.dob.month
        return day == birth_day and month == birth_month


class GalleryImage(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    image = models.ImageField(upload_to='profile_pics')


class DogGalleryImage(models.Model):
    dog = models.ForeignKey(Dog, models.CASCADE)
    image = models.ImageField(upload_to='dog_pics')
