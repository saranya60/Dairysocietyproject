# Generated by Django 4.2.4 on 2023-08-17 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empapp', '0008_remove_salesdb_price_salesdb_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesdb',
            name='Date',
            field=models.DateField(auto_now=True),
        ),
    ]