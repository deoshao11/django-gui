# Generated by Django 3.0.4 on 2020-04-13 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20200409_1729'),
    ]

    operations = [
        migrations.RenameField(
            model_name='internalaccount',
            old_name='isChildAccount',
            new_name='hasParents',
        ),
    ]
