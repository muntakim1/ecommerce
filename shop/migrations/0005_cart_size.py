# Generated by Django 2.2.5 on 2019-09-23 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20190923_1334'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='size',
            field=models.CharField(default='small', max_length=240),
        ),
    ]