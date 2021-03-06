# Generated by Django 3.0.2 on 2020-06-02 10:36

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0008_auto_20200528_0004'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagesProperty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='')),
            ],
        ),
        migrations.RemoveField(
            model_name='property_information',
            name='image',
        ),
        migrations.AlterField(
            model_name='property_information',
            name='amenities',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Gym', 'Gym'), ('Swimming Pool', 'Swimming Pool'), ('Garden', 'Garden'), ('Club House', 'Club House'), ('Cafe Area', 'Cafe Area'), ('Children Play Area', 'Children Play Area'), ('Intercom', 'Intercom'), ('Amphitheatre', 'Amphitheatre'), ('Yoga club', 'Yoga club'), ('Servent room', 'Servent room'), ('High security', 'High security'), ('CCTV camera', 'CCTV camera'), ('Mini banquet', 'Mini banquet')], max_length=148),
        ),
        migrations.AddField(
            model_name='property_information',
            name='images',
            field=models.ManyToManyField(to='properties.ImagesProperty'),
        ),
    ]
