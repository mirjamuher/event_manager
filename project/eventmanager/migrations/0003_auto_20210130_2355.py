# Generated by Django 3.1.5 on 2021-01-30 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventmanager', '0002_auto_20210130_0036'),
    ]

    operations = [
        migrations.RenameField(
            model_name='participant',
            old_name='organisation_name',
            new_name='organisation',
        ),
        migrations.AlterField(
            model_name='participant',
            name='email',
            field=models.EmailField(max_length=250, unique=True),
        ),
    ]
