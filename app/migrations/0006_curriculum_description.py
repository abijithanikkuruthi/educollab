# Generated by Django 2.2.10 on 2020-02-22 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20200222_1141'),
    ]

    operations = [
        migrations.AddField(
            model_name='curriculum',
            name='description',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
