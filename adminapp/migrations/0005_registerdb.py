# Generated by Django 4.2.4 on 2023-08-22 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0004_alter_attendancedb_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='registerdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(blank=True, max_length=50, null=True)),
                ('mobile', models.IntegerField(blank=True, null=True)),
                ('Password', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
