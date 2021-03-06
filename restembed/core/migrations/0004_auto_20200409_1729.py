# Generated by Django 3.0.4 on 2020-04-09 17:29

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200404_1954'),
    ]

    operations = [
        migrations.AddField(
            model_name='internalaccount',
            name='children',
            field=jsonfield.fields.JSONField(default=[]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='internalaccount',
            name='isChildAccount',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
