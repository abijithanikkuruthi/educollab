# Generated by Django 2.2.10 on 2020-03-05 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0028_remove_bit_posted_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='changelog',
            name='bit',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='changelog', to='app.Bit'),
        ),
        migrations.AlterField(
            model_name='changelog',
            name='curriculum',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='changelog', to='app.Curriculum'),
        ),
    ]
