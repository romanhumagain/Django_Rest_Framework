# Generated by Django 4.2.1 on 2023-08-09 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APItest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='age',
            field=models.IntegerField(default=None, null=True),
        ),
    ]
