# Generated by Django 4.1.5 on 2023-02-18 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]