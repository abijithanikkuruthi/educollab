# Generated by Django 2.2.10 on 2020-03-11 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0040_contributor'),
    ]

    operations = [
        migrations.AddField(
            model_name='field',
            name='coverimage',
            field=models.FileField(default=None, null=True, upload_to=''),
        ),
    ]
