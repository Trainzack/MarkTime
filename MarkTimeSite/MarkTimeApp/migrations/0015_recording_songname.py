# Generated by Django 2.2.3 on 2019-08-17 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MarkTimeApp', '0014_auto_20190816_1356'),
    ]

    operations = [
        migrations.AddField(
            model_name='recording',
            name='song_name',
            field=models.CharField(default='', max_length=50),
        ),
    ]
