# Generated by Django 3.0.7 on 2020-07-02 14:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_remove_profile_nationality'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='town',
        ),
    ]
