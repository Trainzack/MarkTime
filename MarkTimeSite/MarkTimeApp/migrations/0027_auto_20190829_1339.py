# Generated by Django 2.2.3 on 2019-08-29 20:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MarkTimeApp', '0026_auto_20190829_1328'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='eboardmember',
            options={'ordering': ['first_name']},
        ),
        migrations.AlterModelOptions(
            name='song',
            options={'ordering': ['song_name']},
        ),
    ]
