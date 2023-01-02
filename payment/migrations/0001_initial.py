# Generated by Django 4.1.2 on 2023-01-02 08:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method', models.CharField(default='Razorpay', max_length=50)),
                ('quantity', models.IntegerField(default=0)),
                ('total_price', models.FloatField(default=0)),
                ('payment_status', models.BooleanField(default=True)),
                ('order_id', models.CharField(default=None, max_length=200, null=True, unique=True)),
                ('datetime_of_payment', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_at', models.TimeField(auto_now=True)),
                ('razorpay_order_id', models.CharField(blank=True, max_length=1000, null=True)),
                ('razorpay_payment_id', models.CharField(blank=True, max_length=1000, null=True)),
                ('razorpay_signature', models.CharField(blank=True, max_length=1000, null=True)),
                ('address', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='user.address')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]