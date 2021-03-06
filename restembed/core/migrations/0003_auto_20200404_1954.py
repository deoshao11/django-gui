# Generated by Django 3.0.4 on 2020-04-04 19:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_accountbalance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountbalance',
            name='accountName',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='externalaccount',
            name='accountName',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='internalaccount',
            name='accountName',
            field=models.CharField(max_length=100),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='requestUuid',
            field=models.UUIDField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='externalaccount',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='externalaccount',
            name='requestUuid',
            field=models.UUIDField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='internalaccount',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='internalaccount',
            name='requestUuid',
            field=models.UUIDField(default=0),
            preserve_default=False,
        )
    ]
