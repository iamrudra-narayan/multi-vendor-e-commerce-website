# Generated by Django 4.1.2 on 2023-01-02 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_order_cart_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='cart_items',
            field=models.CharField(default=None, max_length=2550),
        ),
    ]