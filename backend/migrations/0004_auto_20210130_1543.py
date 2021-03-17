# Generated by Django 3.1.1 on 2021-01-30 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_auto_20210129_0932'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='elivator',
            new_name='elevator',
        ),
        migrations.AlterField(
            model_name='listingimage',
            name='image',
            field=models.ImageField(upload_to='images/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='listingimage',
            name='listing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.listing'),
        ),
    ]