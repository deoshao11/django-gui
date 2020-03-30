# Generated by Django 3.0.4 on 2020-03-30 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExternalAccount',
            fields=[
                ('accountName', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=100)),
                ('exchangeAssociation', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='InternalAccount',
            fields=[
                ('accountName', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('sourceId', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('productAssociation', models.CharField(max_length=100)),
                ('externalAccountAssociation', models.CharField(max_length=100)),
            ],
        ),
    ]
