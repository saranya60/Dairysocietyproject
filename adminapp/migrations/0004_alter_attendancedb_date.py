# Generated by Django 4.2.4 on 2023-08-04 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0003_attendancedb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendancedb',
            name='Date',
            field=models.DateField(auto_now=True),
        ),
    ]
