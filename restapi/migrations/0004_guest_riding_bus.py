# Generated by Django 2.0.3 on 2018-04-11 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0003_auto_20180409_2229'),
    ]

    operations = [
        migrations.AddField(
            model_name='guest',
            name='riding_bus',
            field=models.NullBooleanField(default=None),
        ),
    ]
