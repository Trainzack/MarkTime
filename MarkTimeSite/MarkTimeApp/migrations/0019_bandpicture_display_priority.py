# Generated by Django 2.2.3 on 2019-08-19 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MarkTimeApp', '0018_announcement'),
    ]

    operations = [
        migrations.AddField(
            model_name='bandpicture',
            name='display_priority',
            field=models.IntegerField(default=0),
        ),
    ]
