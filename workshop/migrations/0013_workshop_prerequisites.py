# Generated by Django 3.2 on 2021-12-09 00:20

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshop', '0012_remove_workshop_end_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='workshop',
            name='prerequisites',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), default=list, size=None),
        ),
    ]
