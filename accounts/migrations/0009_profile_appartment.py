# Generated by Django 3.0.7 on 2020-07-01 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_profile_full_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='appartment',
            field=models.CharField(default='', max_length=50, null=True),
        ),
    ]
