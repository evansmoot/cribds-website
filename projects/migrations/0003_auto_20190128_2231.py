# Generated by Django 2.1.5 on 2019-01-29 03:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20190121_1555'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='camp',
            table='camps',
        ),
        migrations.AlterModelTable(
            name='project',
            table='projects',
        ),
        migrations.AlterModelTable(
            name='projecttype',
            table='project_types',
        ),
        migrations.AlterModelTable(
            name='refugee',
            table='refugees',
        ),
        migrations.AlterModelTable(
            name='town',
            table='towns',
        ),
    ]
