# Generated by Django 2.2.3 on 2019-08-22 01:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MarkTimeApp', '0024_auto_20190821_1755'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eboardmember',
            name='is_active_eboard',
        ),
    ]
