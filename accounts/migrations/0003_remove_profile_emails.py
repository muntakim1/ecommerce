# Generated by Django 2.2.8 on 2020-01-25 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200125_2113'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='emails',
        ),
    ]
