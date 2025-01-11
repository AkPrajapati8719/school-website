# Generated by Django 5.1.3 on 2024-12-14 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mySch', '0005_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('father_name', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=15)),
                ('student_id', models.CharField(max_length=30)),
                ('student_class', models.CharField(max_length=50)),
                ('total_fees', models.DecimalField(decimal_places=2, max_digits=10)),
                ('paid_fees', models.DecimalField(decimal_places=2, max_digits=10)),
                ('due_fees', models.DecimalField(decimal_places=2, max_digits=10)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
