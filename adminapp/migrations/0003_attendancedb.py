# Generated by Django 4.2.4 on 2023-08-04 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0002_remove_farmerdb_cardno'),
    ]

    operations = [
        migrations.CreateModel(
            name='attendancedb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateTimeField(auto_now=True)),
                ('Empname', models.CharField(blank=True, max_length=100, null=True)),
                ('Attendance', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
    ]