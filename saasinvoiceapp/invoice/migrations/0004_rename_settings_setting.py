# Generated by Django 3.2.8 on 2021-10-26 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0003_auto_20211026_1347'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Settings',
            new_name='Setting',
        ),
    ]
