# Generated by Django 4.1.5 on 2023-03-26 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0035_rename_dedline_university_deadline_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='apply',
            name='university_name',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
