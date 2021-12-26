# Generated by Django 3.1 on 2020-09-10 17:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dive', '0007_auto_20200910_1739'),
    ]

    operations = [
        migrations.AddField(
            model_name='dive',
            name='bottom_temperature',
            field=models.PositiveIntegerField(default=15, help_text='Bottom temperature in degree celsius.', validators=[django.core.validators.MaxValueValidator(60)]),
        ),
        migrations.AddField(
            model_name='dive',
            name='surface_temperature',
            field=models.PositiveIntegerField(default=30, help_text='Surface temperature in degree celsius.', validators=[django.core.validators.MaxValueValidator(60)]),
        ),
        migrations.AlterField(
            model_name='dive',
            name='max_depth',
            field=models.PositiveIntegerField(default=30, validators=[django.core.validators.MaxValueValidator(5000)]),
        ),
        migrations.AlterField(
            model_name='dive',
            name='visibility',
            field=models.PositiveIntegerField(default=20, help_text='Visibility in metres.', validators=[django.core.validators.MaxValueValidator(1000)]),
        ),
    ]