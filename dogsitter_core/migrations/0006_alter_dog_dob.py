# Generated by Django 4.0.6 on 2022-07-13 18:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dogsitter_core', '0005_alter_dog_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='dob',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
