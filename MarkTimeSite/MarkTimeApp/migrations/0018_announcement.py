# Generated by Django 2.2.3 on 2019-08-19 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MarkTimeApp', '0017_auto_20190816_1826'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('information', models.TextField(max_length=1000)),
            ],
        ),
    ]
