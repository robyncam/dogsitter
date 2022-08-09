# Generated by Django 4.0.6 on 2022-08-09 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dogsitter_core', '0030_alter_profile_housing'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='living_arrangements',
            field=models.CharField(choices=[('I live alone', 'I live alone'), ('I live with my spouse/partner', 'I live with my spouse/partner'), ('I live with roommates', 'I live with roommates'), ('I live with my spouse and children', 'I live with my spouse and children'), ('I live with children', 'I live with children')], default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='housing',
            field=models.CharField(choices=[('I live in a house', 'I live in a house'), ('I live in an apartment', 'I live in an apartment'), ('I live in a condo', 'I live in a condo'), ('I live in an alternative style of housing', 'I live in an alternative style of housing')], default='', max_length=100),
        ),
    ]