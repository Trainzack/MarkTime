# Generated by Django 2.2.3 on 2019-08-02 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MarkTimeApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eboardmember',
            name='eboard_position',
            field=models.CharField(choices=[('President', 'President'), ('Vice President', 'Vice President'), ('Director', 'Director'), ('Assistant Director', 'Assistant Director'), ('Secretary', 'Secretary'), ('Treasurer', 'Treasurer'), ('Membership Chair', 'Membership Chair'), ('Librarian', 'Librarian'), ('Property Manager', 'Property Manager'), ('Historian', 'Historian'), ('Webmaster', 'Webmaster'), ('Section Leader', 'Section Leader')], max_length=20),
        ),
    ]
