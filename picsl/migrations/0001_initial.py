# Generated by Django 3.1.4 on 2022-05-01 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='nblogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=300)),
                ('desc', models.TextField(max_length=4000)),
                ('date', models.DateField()),
                ('img', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='nevents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('desc', models.TextField(max_length=4000)),
                ('img', models.ImageField(upload_to='')),
                ('date', models.DateField()),
                ('link', models.URLField(max_length=500, unique=True)),
            ],
        ),
    ]
