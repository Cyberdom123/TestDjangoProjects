# Generated by Django 3.2.6 on 2021-08-19 14:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(default=django.utils.timezone.now, max_length=32),
            preserve_default=False,
        ),
    ]
