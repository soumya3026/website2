# Generated by Django 3.2 on 2022-04-30 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_fac'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fac',
            name='pic',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
