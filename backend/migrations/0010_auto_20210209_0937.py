# Generated by Django 3.1.1 on 2021-02-09 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0009_auto_20210208_1910'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='listing',
            options={'ordering': ['-created']},
        ),
    ]
