# Generated by Django 2.2.8 on 2020-01-25 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20200125_2152'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='country',
            field=models.CharField(default='', max_length=50),
        ),
    ]
