# Generated by Django 2.2.10 on 2020-02-24 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20200224_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bit',
            name='file',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='bit', to='app.File'),
        ),
        migrations.AlterField(
            model_name='bit',
            name='url',
            field=models.CharField(blank=True, max_length=512),
        ),
        migrations.AlterField(
            model_name='curriculum',
            name='description',
            field=models.CharField(blank=True, default='', max_length=1000),
        ),
    ]