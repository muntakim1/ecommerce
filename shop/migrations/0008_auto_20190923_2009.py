# Generated by Django 2.2.5 on 2019-09-23 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20190923_1513'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='product',
            index_together={('id', 'Product_slug')},
        ),
    ]