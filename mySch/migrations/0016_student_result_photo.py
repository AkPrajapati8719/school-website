# Generated by Django 5.1.3 on 2025-01-21 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mySch', '0015_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='result_photo',
            field=models.ImageField(blank=True, null=True, upload_to='result_photos/'),
        ),
    ]
