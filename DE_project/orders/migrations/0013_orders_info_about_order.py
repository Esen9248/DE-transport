# Generated by Django 2.0.4 on 2018-04-30 13:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_auto_20180427_1411'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='info_about_order',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
