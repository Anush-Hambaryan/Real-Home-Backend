# Generated by Django 3.1.1 on 2021-02-09 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0010_auto_20210209_0937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
