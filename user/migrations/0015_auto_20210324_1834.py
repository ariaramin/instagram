# Generated by Django 3.1.6 on 2021-03-24 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0014_auto_20210324_1826'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='last_name',
        ),
    ]
