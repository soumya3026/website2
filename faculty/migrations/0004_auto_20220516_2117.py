# Generated by Django 3.1.4 on 2022-05-16 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0003_alter_faprofile_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faprofile',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
