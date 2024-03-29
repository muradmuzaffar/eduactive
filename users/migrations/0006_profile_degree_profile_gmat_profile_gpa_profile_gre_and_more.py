# Generated by Django 4.1.5 on 2023-03-09 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_profile_birthday_profile_gender_profile_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='degree',
            field=models.CharField(blank=True, choices=[('Bachelor', 'Bachelor'), ('Master', 'Master'), ('Ph.D.', 'Ph.D.'), ('Exchange programme', 'Exchange programme'), ('Training programme', 'Training programme')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='gmat',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='gpa',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='gre',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='ielts',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='speciality',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='toefl',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='university',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
