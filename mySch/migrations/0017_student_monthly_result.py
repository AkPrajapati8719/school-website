# Generated by Django 5.1.3 on 2025-01-21 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mySch', '0016_student_result_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='monthly_result',
            field=models.IntegerField(default=20, max_length=2),
            preserve_default=False,
        ),
    ]
