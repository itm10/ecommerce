# Generated by Django 5.0 on 2023-12-21 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='in_discount_price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
