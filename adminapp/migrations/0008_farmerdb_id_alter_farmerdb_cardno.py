# Generated by Django 4.2.4 on 2023-08-24 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0007_alter_farmerdb_cardno'),
    ]

    operations = [
        migrations.AddField(
            model_name='farmerdb',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='farmerdb',
            name='Cardno',
            field=models.IntegerField(default='null', unique=True),
        ),
    ]
