# Generated by Django 4.2.4 on 2023-08-24 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0014_farmerdb_delete_farmersdb'),
    ]

    operations = [
        migrations.AddField(
            model_name='farmerdb',
            name='Cardno',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]