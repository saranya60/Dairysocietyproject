# Generated by Django 4.2.4 on 2023-09-12 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empapp', '0017_invoicedb'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoicedb',
            name='Customer',
        ),
    ]