# Generated by Django 3.1 on 2020-08-13 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0003_auto_20200813_0943'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user_name',
        ),
    ]
