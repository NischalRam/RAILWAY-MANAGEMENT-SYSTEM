# Generated by Django 3.1.4 on 2020-12-12 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trains', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='customer',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='booking',
            name='phone',
            field=models.CharField(max_length=10),
        ),
    ]