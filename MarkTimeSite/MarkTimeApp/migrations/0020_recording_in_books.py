# Generated by Django 2.2.3 on 2019-08-19 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MarkTimeApp', '0019_bandpicture_display_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='recording',
            name='in_books',
            field=models.BooleanField(default=False),
        ),
    ]