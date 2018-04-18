# Generated by Django 2.0.4 on 2018-04-18 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20180416_1442'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='slug',
            field=models.SlugField(default=2, max_length=100, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='orders',
            name='place',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]