# Generated by Django 4.2.4 on 2023-08-17 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empapp', '0005_alter_productdb_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdb',
            name='Price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='salesdb',
            name='Price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='salesdb',
            name='Quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
