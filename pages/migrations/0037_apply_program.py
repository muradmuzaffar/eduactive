# Generated by Django 4.1.5 on 2023-03-26 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0036_apply_university_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='apply',
            name='program',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
