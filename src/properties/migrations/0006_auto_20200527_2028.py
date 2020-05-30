# Generated by Django 3.0.2 on 2020-05-27 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0005_auto_20200527_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property_information',
            name='BHK',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='property_information',
            name='furnishing',
            field=models.CharField(choices=[('Un-Furnished', 'Un-Furnished'), ('Semi-Furnished', 'Semi-Furnished'), ('Furnished', 'Furnished'), ('Fully-Furnished', 'Fully-Furnished')], max_length=100),
        ),
    ]
