# Generated by Django 3.1.6 on 2021-03-24 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_remove_profile_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='media/user/images/user.png', upload_to='media/user/images'),
        ),
    ]
