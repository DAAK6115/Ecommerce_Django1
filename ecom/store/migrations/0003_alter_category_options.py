# Generated by Django 5.0.4 on 2024-04-07 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_is_sale_product_sale_price'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
    ]