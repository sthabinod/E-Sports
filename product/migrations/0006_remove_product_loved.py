# Generated by Django 3.2 on 2021-08-24 02:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_product_loved'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='loved',
        ),
    ]