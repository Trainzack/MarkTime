# Generated by Django 2.2.3 on 2019-08-22 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MarkTimeApp', '0023_auto_20190821_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bandpicture',
            name='picture_file',
            field=models.ImageField(upload_to='pictures/band'),
        ),
        migrations.AlterField(
            model_name='eboardmember',
            name='eboard_picture',
            field=models.ImageField(upload_to='pictures/eboard'),
        ),
    ]
