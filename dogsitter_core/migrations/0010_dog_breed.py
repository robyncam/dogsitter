# Generated by Django 4.0.6 on 2022-07-15 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dogsitter_core', '0009_alter_dog_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='dog',
            name='breed',
            field=models.CharField(default=False, max_length=1000),
        ),
    ]
