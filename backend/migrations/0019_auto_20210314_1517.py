# Generated by Django 3.1.1 on 2021-03-14 15:17

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0018_auto_20210314_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listingimage',
            name='image_medium',
            field=imagekit.models.fields.ProcessedImageField(upload_to='images/%Y/%m/%d'),
        ),
    ]
