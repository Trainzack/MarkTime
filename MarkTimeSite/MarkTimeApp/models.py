from django.db import models
from .validators import validate_recording_file_extension
from PIL import Image
import datetime
# Create your models here.


# This class is used to store a band's year in review, it contains the year, a summary of what happened in that year,
# and pictures associated with that year.
class HistoryYear(models.Model):
    year = models.IntegerField(unique=True)
    summary = models.TextField()
    # Place another attribute here for keys to multiple pictures

    def __str__(self):
        return "History for the year " + str(self.year)


# This class exists to aid in deleting BandPictures through the admin page
# It allows a group of BandPicture to be selected and all delete their picture files upon deletion
class BandPictureQuerySet(models.QuerySet):
    def delete(self, *args, **kwargs):
        for obj in self:
            obj.picture_file.delete()
        super(BandPictureQuerySet, self).delete(*args, **kwargs)


# This class is used to store a picture of the band
# That picture can be of an eboard member or of the band
# fields include the picture file, whether it appears on the front page of the site, a caption,
# alt text for the picture, and the date it was taken
class BandPicture(models.Model):
    objects = BandPictureQuerySet.as_manager()

    picture_file = models.ImageField(upload_to="pictures/band", null=False)
    on_front_page = models.BooleanField()
    display_priority = models.IntegerField(default=0)
    caption = models.TextField(max_length=200)
    alt_text = models.TextField(max_length=200)
    date_taken = models.DateField(default=datetime.date.today)
    # NOTE: Consider removing associated_history_year field and instead populate a history year's page with pictures
    # by using database queries filtered by dates instead
    associated_history_year = models.ForeignKey(HistoryYear, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return str(self.picture_file)

    def delete(self, *args, **kwargs):
        self.picture_file.delete()
        super(BandPicture, self).delete(*args,**kwargs)

    # Overridden save method that resizes images to 1280x720 Currently not in use
    # def save(self, *args, **kwargs):
    #    super(BandPicture,self).save(*args, **kwargs)
    #    image = Image.open(self.picture_file.path)
    #    image = image.resize((1280,720),Image.ANTIALIAS)
    #    image.save(self.picture_file.path)


# This class exists to aid in deleting BandPictures through the admin page
# It allows a group of BandPicture to be selected and all delete their picture files upon deletion
class EboardMemberQuerySet(models.QuerySet):
    def delete(self, *args, **kwargs):
        for obj in self:
            obj.eboard_picture.delete()
        super(EboardMemberQuerySet, self).delete(*args, **kwargs)


# This class is used to store an eboard member
# Fields include first name, last name, eboard position, an about_me section, and a picture
# Eboard member objects have a one to one relationship with a given picture. Ideally that picture
# is of the eboard member.
class EboardMember(models.Model):
    objects = EboardMemberQuerySet.as_manager()

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
        ('Section Leader', 'Section Leader'),
        ('Advisor', 'Advisor')
    )
    eboard_position = models.CharField(max_length=20, choices=EBOARD_POSITIONS)
    about_me = models.TextField()
    # is_active_eboard = models.BooleanField(default=True)
    eboard_picture = models.ImageField(upload_to="pictures/eboard")

    def __str__(self):
        info_string = self.first_name + " " + self.last_name
        # info_string += "\n" + self.eboard_position
        # info_string += "\n" + self.about_me
        return info_string

    def delete(self, *args, **kwargs):
        self.eboard_picture.delete()
        super(EboardMember, self).delete(*args,**kwargs)


# The recording class is used to store a song's audio recording
# Fields include the recording's file (which is validated using a custom validator), the date is was recorded,
# who performed the song, and the event it was performed at.
class Recording(models.Model):
    recording_file = models.FileField(upload_to='recordings', validators=[validate_recording_file_extension], null=True)
    date_recorded = models.DateField(default=datetime.date.today)
    performer = models.CharField(max_length=50)
    event = models.CharField(max_length=50)
    songname = models.CharField(max_length=50, default='')
    artist = models.CharField(max_length=50, default='')
    in_books = models.BooleanField(default=False)
    # associated_song = models.ForeignKey(Song,on_delete=models.SET_NULL,null=True,blank=True)

    def __str__(self):
        return str(self.songname)

    def delete(self, *args, **kwargs):
        self.recording_file.delete()
        super(Recording, self).delete(*args, **kwargs)


# FAQ class is used to store FAQ regarding the band
class FAQ(models.Model):
    question = models.TextField(max_length=1000)
    answer = models.TextField(max_length=1000)

    def __str__(self):
        return "Q: " + self.question


class Announcement(models.Model):
    title = models.CharField(max_length=30)
    information = models.TextField(max_length=1000)

    def __str__(self):
        return self.title