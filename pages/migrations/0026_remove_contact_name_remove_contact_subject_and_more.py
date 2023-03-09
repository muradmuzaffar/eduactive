# Generated by Django 4.1.5 on 2023-02-19 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0025_alter_scholarship_region_alter_university_degree'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='name',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='subject',
        ),
        migrations.AddField(
            model_name='contact',
            name='first_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='last_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='number',
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(blank=True, null=True),
        ),
    ]