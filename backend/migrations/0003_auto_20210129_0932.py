# Generated by Django 3.1.1 on 2021-01-29 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20210128_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listingimage',
            name='image',
            field=models.ImageField(default='', upload_to='images/'),
            preserve_default=False,
        ),
    ]