# Generated by Django 3.2.9 on 2022-02-19 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20220219_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='project_id',
            field=models.CharField(max_length=14),
        ),
    ]