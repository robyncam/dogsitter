from django.contrib import admin
from .models import Profile, Dog, DogSitterProfile

# Register your models here.

admin.site.register(Profile)
admin.site.register(Dog)
admin.site.register(DogSitterProfile)
