# Generated by Django 2.2.3 on 2019-08-07 05:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MarkTimeApp', '0009_auto_20190806_2252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eboardmember',
            name='eboard_picture',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='MarkTimeApp.BandPicture'),
        ),
    ]
