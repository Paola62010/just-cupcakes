# Generated by Django 3.2 on 2022-03-26 18:18

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('careers', '0004_alter_jobapplication_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobapplication',
            name='resume',
            field=cloudinary.models.CloudinaryField(max_length=255),
        ),
    ]
