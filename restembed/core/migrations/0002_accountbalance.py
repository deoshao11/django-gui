# Generated by Django 3.0.4 on 2020-04-02 19:10

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountBalance',
            fields=[
                ('accountName', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=100)),
                ('instruments', jsonfield.fields.JSONField()),
            ],
        ),
    ]
