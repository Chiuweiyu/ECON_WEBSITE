# Generated by Django 3.0.2 on 2020-02-19 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200219_1314'),
    ]

    operations = [
        migrations.CreateModel(
            name='proInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('slug', models.CharField(max_length=20)),
                ('body', models.TextField()),
            ],
        ),
    ]
