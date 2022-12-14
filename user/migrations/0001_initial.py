# Generated by Django 4.1.2 on 2023-01-01 06:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Adminshoppost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_name', models.CharField(default='name', max_length=30)),
                ('shop_banner', models.ImageField(default='', upload_to='pics/shopbanner')),
                ('shop_details', models.TextField(default='', max_length=300)),
                ('shop_address', models.TextField(default='', max_length=100)),
                ('mobile', models.CharField(default='', max_length=13)),
                ('email', models.EmailField(default='', max_length=30)),
                ('open_time', models.TextField(default='11AM', max_length=6)),
                ('close_time', models.TextField(default='10PM', max_length=6)),
                ('open_status', models.BooleanField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Userprofile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.CharField(default='Null', max_length=3)),
                ('gender', models.CharField(default='Null', max_length=8)),
                ('user_model', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('pincode', models.IntegerField(default='')),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(default='Choudwar', max_length=100)),
                ('dist', models.CharField(default='Cuttack', max_length=100)),
                ('state', models.CharField(default='Odisha', max_length=100)),
                ('mobile', models.IntegerField()),
                ('s_mobile', models.IntegerField()),
                ('place', models.CharField(default='', max_length=5)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
