# Generated by Django 2.2.3 on 2019-08-29 21:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MarkTimeApp', '0028_auto_20190829_1340'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='historyyear',
            options={'ordering': ['-year']},
        ),
    ]
