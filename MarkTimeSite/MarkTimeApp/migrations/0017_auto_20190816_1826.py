# Generated by Django 2.2.3 on 2019-08-17 01:26

import MarkTimeApp.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MarkTimeApp', '0016_recording_artist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recording',
            name='recording_file',
            field=models.FileField(null=True, upload_to='recordings', validators=[MarkTimeApp.validators.validate_recording_file_extension]),
        ),
    ]
