# Generated by Django 2.2.5 on 2019-09-23 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_product_stars'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='new_Arraivel',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='stars',
            field=models.IntegerField(default=4),
        ),
    ]
