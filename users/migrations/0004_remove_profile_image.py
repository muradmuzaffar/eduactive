# Generated by Django 4.1.5 on 2023-03-08 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_rename_name_profile_first_name_profile_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='image',
        ),
    ]
