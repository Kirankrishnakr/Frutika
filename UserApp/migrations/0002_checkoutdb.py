# Generated by Django 3.2.10 on 2023-06-10 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckoutDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FullName', models.CharField(blank=True, max_length=40, null=True)),
                ('Email', models.EmailField(blank=True, max_length=40, null=True)),
                ('State', models.CharField(blank=True, max_length=40, null=True)),
                ('Address', models.CharField(blank=True, max_length=200, null=True)),
                ('Town', models.CharField(blank=True, max_length=50, null=True)),
                ('Landmark', models.CharField(blank=True, max_length=50, null=True)),
                ('Pincode', models.CharField(blank=True, max_length=50, null=True)),
                ('PhoneNumber', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]