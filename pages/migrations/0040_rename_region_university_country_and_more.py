# Generated by Django 4.1.5 on 2023-05-05 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0039_apply_gmat_apply_gre_apply_ielts_apply_toefl'),
    ]

    operations = [
        migrations.RenameField(
            model_name='university',
            old_name='region',
            new_name='country',
        ),
        migrations.RenameField(
            model_name='university',
            old_name='graduation_rate',
            new_name='state_city',
        ),
        migrations.RemoveField(
            model_name='university',
            name='acceptance_rate',
        ),
        migrations.RemoveField(
            model_name='university',
            name='city',
        ),
        migrations.RemoveField(
            model_name='university',
            name='fee_waiver',
        ),
        migrations.RemoveField(
            model_name='university',
            name='link',
        ),
        migrations.RemoveField(
            model_name='university',
            name='other_email',
        ),
        migrations.RemoveField(
            model_name='university',
            name='result',
        ),
        migrations.RemoveField(
            model_name='university',
            name='state',
        ),
        migrations.AddField(
            model_name='university',
            name='qs_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]