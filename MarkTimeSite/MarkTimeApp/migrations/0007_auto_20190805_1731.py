# Generated by Django 2.2.3 on 2019-08-06 00:31

import MarkTimeApp.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MarkTimeApp', '0006_auto_20190805_1647'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recording',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recording_file', models.FileField(upload_to='recordings', validators=[MarkTimeApp.validators.validate_recording_file_extension])),
                ('performer', models.CharField(max_length=25)),
                ('event', models.CharField(max_length=25)),
            ],
        ),
        migrations.AlterField(
            model_name='bandpicture',
            name='associated_history_year',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='MarkTimeApp.HistoryYear'),
        ),
        migrations.AlterField(
            model_name='eboardmember',
            name='eboard_picture',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='MarkTimeApp.BandPicture'),
        ),
    ]
