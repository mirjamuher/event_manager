# Generated by Django 3.1.5 on 2021-01-30 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventmanager', '0001_initial'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='event',
            constraint=models.UniqueConstraint(fields=('name', 'date'), name='unique_event'),
        ),
    ]