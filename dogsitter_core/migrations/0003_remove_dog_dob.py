# Generated by Django 4.0.6 on 2022-07-13 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dogsitter_core', '0002_dog'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dog',
            name='dob',
        ),
    ]
