# Generated by Django 4.2.1 on 2023-08-08 05:26

from django.db import migrations, models
import django.db.models.fields.related


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='StudentInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=100)),
                ('course', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('skill', models.ForeignKey(default=None, null=True, on_delete=django.db.models.fields.related.ForeignKey, to='home.skill')),
            ],
        ),
    ]
