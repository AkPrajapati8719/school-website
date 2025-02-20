# Generated by Django 5.1.3 on 2025-01-06 09:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mySch', '0014_delete_studentauth'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('account_id', models.CharField(max_length=50, unique=True)),
                ('identity', models.CharField(choices=[('student', 'Student'), ('teacher', 'Teacher')], max_length=10)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('paid_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('due_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mySch.student')),
                ('teacher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mySch.teacher')),
            ],
        ),
    ]
