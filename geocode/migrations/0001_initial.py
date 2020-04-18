# Generated by Django 3.0.5 on 2020-04-18 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geocode', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=500)),
                ('city', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'profiles_country',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Coordinate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=150)),
            ],
        ),
    ]
