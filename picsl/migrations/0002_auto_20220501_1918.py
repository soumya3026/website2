# Generated by Django 3.1.4 on 2022-05-01 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('picsl', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=300)),
                ('desc', models.TextField(max_length=4000)),
                ('date', models.DateField()),
                ('img', models.ImageField(upload_to='')),
            ],
        ),
        migrations.DeleteModel(
            name='nblogs',
        ),
    ]
