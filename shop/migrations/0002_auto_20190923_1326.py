# Generated by Django 2.2.5 on 2019-09-23 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_images',
            name='image_1',
            field=models.ImageField(blank=True, upload_to='product/%Y/%m/%d/'),
        ),
    ]
