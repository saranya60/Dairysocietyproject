# Generated by Django 4.2.4 on 2023-08-21 20:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empapp', '0015_rename_milkevg_milkdb_milk_remove_milkdb_cardno_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='milkdb',
            name='Total',
        ),
    ]
