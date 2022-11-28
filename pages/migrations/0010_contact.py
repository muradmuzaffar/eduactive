# Generated by Django 4.1.3 on 2022-11-26 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_university_bio_alter_university_admission_req'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.TextField(blank=True)),
            ],
        ),
    ]