# Generated by Django 3.1.4 on 2022-05-20 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_auto_20220516_2117'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='face',
            name='file',
        ),
    ]
