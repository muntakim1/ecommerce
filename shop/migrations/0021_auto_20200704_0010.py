# Generated by Django 3.0.8 on 2020-07-03 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0020_auto_20200704_0009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions',
            name='Total',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
    ]
