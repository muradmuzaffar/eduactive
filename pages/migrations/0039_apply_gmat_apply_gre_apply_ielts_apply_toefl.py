# Generated by Django 4.1.5 on 2023-03-26 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0038_apply_gpa'),
    ]

    operations = [
        migrations.AddField(
            model_name='apply',
            name='gmat',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='apply',
            name='gre',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='apply',
            name='ielts',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='apply',
            name='toefl',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]