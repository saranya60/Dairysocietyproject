# Generated by Django 4.2.4 on 2023-08-21 18:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empapp', '0014_milkdb_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='milkdb',
            old_name='Milkevg',
            new_name='Milk',
        ),
        migrations.RemoveField(
            model_name='milkdb',
            name='Cardno',
        ),
        migrations.RemoveField(
            model_name='milkdb',
            name='Milkmng',
        ),
    ]
