# Generated by Django 4.0.6 on 2022-08-10 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dogsitter_core', '0043_alter_dogsitterprofile_hours_alone_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='is_dog_sitter',
        ),
    ]
