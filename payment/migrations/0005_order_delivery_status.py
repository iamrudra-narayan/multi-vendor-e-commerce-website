# Generated by Django 4.1.2 on 2023-01-05 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0004_order_prod_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delivery_status',
            field=models.BooleanField(default=False),
        ),
    ]
