# Generated by Django 4.1.5 on 2023-02-12 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0022_alter_scholarship_dedline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scholarship',
            name='name',
            field=models.CharField(max_length=250),
        ),
    ]
