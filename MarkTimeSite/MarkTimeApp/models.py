from django.db import models
from .validators import validate_recording_file_extension
import datetime
# Create your models here.


# This class is used to store a band's year in review, it contains the year, a summary of what happened in that year,
# and pictures associated with that year.
class HistoryYear(models.Model):
    year = models.IntegerField()
    summary = models.TextField()
    # Place another attribute here for keys to multiple pictures

    def __str__(self):
        return "History for the year " + str(self.year)


# This class is used to store a picture of the band
# That picture can be of an eboard member or of the band
# fields include the picture file, whether it appears on the front page of the site, a caption,
# alt text for the picture, and the date it was taken
class BandPicture(models.Model):
    picture_file = models.ImageField(upload_to="pictures")
    on_front_page = models.BooleanField()
    caption = models.TextField(max_length=200)
    alt_text = models.TextField(max_length=200)
    date_taken = models.DateField(default=datetime.date.today)
    # NOTE: Consider removing associated_history_year field and instead populate a history year's page with pictures
    # by using database queries filtered by dates instead
    associated_history_year = models.ForeignKey(HistoryYear, on_delete=models.CASCADE, null=True,blank=True)

    def __str__(self):
        return str(self.picture_file)


# This class is used to store an eboard member
# Fields include first name, last name, eboard position, an about_me section, and a picture
# Eboard member objects have a one to one relationship with a given picture. Ideally that picture
# is of the eboard member.
class EboardMember(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    # These are the possible eboard positions a member can hold
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

    # Create a one to one relationship with a picture of the eboard member
    # on_delete set to SET_NULL so a picture being deleted doesn't delete the eboard member
    eboard_picture = models.OneToOneField(BandPicture,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        info_string = self.first_name + " " + self.last_name
        # info_string += "\n" + self.eboard_position
        # info_string += "\n" + self.about_me
        return info_string


# The recording class is used to store a song's audio recording
# Fields include the recording's file (which is validated using a custom validator), the date is was recorded,
# who performed the song, and the event it was performed at.
class Recording(models.Model):
    recording_file = models.FileField(upload_to='recordings',validators=[validate_recording_file_extension])
    date_recorded = models.DateField
    performer = models.CharField(max_length = 25)
    event = models.CharField(max_length = 25)
    #associated_song = models.ForeignKey(Song,on_delete=models.SET_NULL,null=True,blank=True)

    def __str__(self):
        return str(self.recording_file)


#FAQ class is used to store FAQ regarding the band
class FAQ(models.Model):
    question = models.TextField(max_length=200)
    answer = models.TextField(max_length=200)

    def __str__(self):
        return "Q: " + self.question + " A: " + self.answer