# Generated by Django 3.1.6 on 2021-03-24 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0011_post_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='like',
        ),
    ]
