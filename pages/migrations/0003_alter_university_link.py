# Generated by Django 4.1.3 on 2022-11-14 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_university_gmat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='university',
            name='link',
            field=models.CharField(max_length=200),
        ),
    ]
