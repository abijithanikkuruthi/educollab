# Generated by Django 2.2.10 on 2020-02-22 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20200222_1346'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(default='', max_length=1000)),
                ('url', models.CharField(max_length=512)),
                ('curriculum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bit', to='app.Curriculum')),
                ('file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bit', to='app.File')),
                ('file_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bit', to='app.FileType')),
            ],
        ),
    ]