# Generated by Django 2.0.3 on 2018-04-09 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0002_auto_20180408_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitation',
            name='access_code',
            field=models.CharField(blank=True, max_length=48, null=True),
        ),
    ]
