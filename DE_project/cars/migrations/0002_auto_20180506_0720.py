# Generated by Django 2.0.4 on 2018-05-06 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cars',
            name='volume',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
