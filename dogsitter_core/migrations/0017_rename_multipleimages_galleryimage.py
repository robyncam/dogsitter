# Generated by Django 4.0.6 on 2022-07-21 19:44

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dogsitter_core', '0016_rename_images_multipleimages_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MultipleImages',
            new_name='GalleryImage',
        ),
    ]
