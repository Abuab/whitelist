# Generated by Django 2.1 on 2020-01-13 21:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('whitelist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ip',
            name='update',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
