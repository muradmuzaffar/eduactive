# Generated by Django 4.1.5 on 2023-01-30 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0013_blogs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='quote',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
