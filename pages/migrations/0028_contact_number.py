# Generated by Django 4.1.5 on 2023-02-19 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0027_remove_contact_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='number',
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
    ]
