# Generated by Django 2.2.8 on 2020-02-24 17:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_auto_20200224_1733'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='image_path', to='app.File'),
        ),
    ]
