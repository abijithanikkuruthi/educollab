# Generated by Django 2.2.10 on 2020-02-22 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Upvote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='upvote', to='app.Bit')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='upvote', to='app.Member')),
            ],
        ),
    ]
