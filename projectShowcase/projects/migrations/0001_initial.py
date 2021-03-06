# Generated by Django 3.2.9 on 2022-02-19 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=60)),
                ('project_id', models.CharField(max_length=10)),
                ('project_desc', models.TextField()),
                ('project_contributor_1', models.CharField(max_length=20)),
                ('project_contributor_2', models.CharField(max_length=20)),
                ('project_contributor_3', models.CharField(max_length=20)),
                ('project_contributor_4', models.CharField(max_length=20)),
                ('year', models.IntegerField()),
                ('project_image_1', models.ImageField(upload_to='')),
                ('project_image_2', models.ImageField(upload_to='')),
                ('project_tech', models.TextField()),
            ],
        ),
    ]
