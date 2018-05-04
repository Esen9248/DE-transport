# Generated by Django 2.0.4 on 2018-04-27 13:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_auto_20180427_1326'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='time_for_order',
            new_name='time_from',
        ),
        migrations.AddField(
            model_name='orders',
            name='time_to',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]