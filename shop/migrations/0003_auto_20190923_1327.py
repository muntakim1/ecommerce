# Generated by Django 2.2.5 on 2019-09-23 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20190923_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_images',
            name='image_2',
            field=models.ImageField(blank=True, upload_to='product/%Y/%m/%d/'),
        ),
    ]
