# Generated by Django 2.0.4 on 2018-04-16 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20180416_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='middle_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='users',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='slug',
            field=models.SlugField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='sur_name',
            field=models.CharField(max_length=255),
        ),
    ]
