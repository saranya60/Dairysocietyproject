# Generated by Django 4.2.4 on 2023-08-21 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empapp', '0010_salesdb_price_alter_productdb_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='billdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField(auto_now=True)),
                ('Customer', models.CharField(blank=True, max_length=100, null=True)),
                ('Total', models.FloatField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]