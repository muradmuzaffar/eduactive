# Generated by Django 4.1.5 on 2023-02-01 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0018_alter_blogs_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='created_at',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
