# Generated by Django 4.0.6 on 2022-07-13 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dogsitter_core', '0006_alter_dog_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='dob',
            field=models.DateField(),
        ),
    ]
