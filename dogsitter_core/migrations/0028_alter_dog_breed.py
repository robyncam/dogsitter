# Generated by Django 4.0.6 on 2022-08-16 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dogsitter_core', '0027_alter_dog_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='breed',
            field=models.CharField(max_length=1000),
        ),
    ]
