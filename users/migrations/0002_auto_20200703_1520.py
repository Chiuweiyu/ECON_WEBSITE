# Generated by Django 3.0.6 on 2020-07-03 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Strategy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produce', models.CharField(max_length=500)),
                ('combine', models.CharField(max_length=500)),
                ('research', models.CharField(max_length=500)),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
