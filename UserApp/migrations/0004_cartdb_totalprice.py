# Generated by Django 3.2.10 on 2023-06-24 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0003_auto_20230617_1743'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartdb',
            name='TotalPrice',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
