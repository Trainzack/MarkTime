from django.db import models

# Create your models here.


class EboardMember(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    EBOARD_POSITIONS = (
        ('President', 'President'),
        ('Vice President', 'Vice President'),
        ('Director', 'Director'),
        ('Assistant Director', 'Assistant Director'),
        ('Secretary', 'Secretary'),
        ('Treasurer', 'Treasurer'),
        ('Membership Chair', 'Membership Chair'),
        ('Librarian', 'Librarian'),
        ('Property Manager', 'Property Manager'),
        ('Historian', 'Historian'),
        ('Webmaster', 'Webmaster'),
        ('Section Leader', 'Section Leader')
    )
    eboard_position = models.CharField(max_length=20, choices=EBOARD_POSITIONS)
    about_me = models.TextField()
    # Place another attribute here for a key to a picture once that's figured out

    def __str__(self):
        info_string = self.first_name + " " + self.last_name
        # info_string += "\n" + self.eboard_position
        # info_string += "\n" + self.about_me
        return info_string


class HistoryYear(models.Model):
    year = models.IntegerField()
    Summary = models.TextField()
    # Place another attribute here for keys to multiple pictures

    def __str__(self):
        return "History for the year " + self.year