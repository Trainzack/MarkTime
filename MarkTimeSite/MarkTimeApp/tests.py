from django.test import TestCase
from .models import BandPicture, HistoryYear, EboardMember

# This import is for a mock image upload for our test cases
from django.core.files.uploadedfile import SimpleUploadedFile


# Helper Methods here
def create_band_picture(cap="Test caption"):
    # Create band picture and fill its attributes
    picture = BandPicture()
    picture.picture_file = SimpleUploadedFile(name='test_image.jpg',
                                              content=open('./media/pictures/test_image.jpg', 'rb').read(),
                                              content_type='image/jpeg')
    picture.on_front_page = False
    picture.alt_text = "Test picture"
    picture.caption = cap
    return picture


def create_eboard_member(member_picture, f_name = "Dummy",l_name = "Name"):
    eboard_member = EboardMember(first_name=f_name, last_name=l_name)
    eboard_member.eboard_picture = member_picture
    eboard_member.about_me = "Hello"
    eboard_member.eboard_position = "President"
    return eboard_member


# Create your tests here.


class PictureRelationsTests(TestCase):
    def test_eboard_member_still_exists_after_deleting_band_picture_its_related_to(self):
        # Create BandPicture
        picture = create_band_picture()
        picture.save()

        # Create EboardMember
        eboard_member = create_eboard_member(picture,"Dummy","Name")
        eboard_member.save()

        # Delete the picture and check to assert that the eboard member its associated with still exists
        picture.delete()
        self.assertIs(EboardMember.objects.filter(first_name="Dummy",last_name="Name").exists(),True)

        # Delete remaining objects
        eboard_member.delete()

    def test_band_picture_still_exists_after_deleting_eboard_member_its_reltated_to(self):
        filter_caption = "Test caption"
        # Create BandPicture
        picture = create_band_picture(filter_caption)
        picture.save()

        # Create EboardMember
        eboard_member = create_eboard_member(picture,"Dummy","Name")
        eboard_member.save()

        # Delete the EboardMember and check to assert that the picture its associated with still exists
        eboard_member.delete()

        # Delete picture file
        picture.picture_file.delete()
        self.assertIs(BandPicture.objects.filter(caption=filter_caption).exists(),True)

    def test_history_year_still_exists_after_deleting_band_picture_its_related_to(self):
        test_year = 1990
        # Create BandPicture
        picture = create_band_picture()
        picture.save()

        # Create the history year and add it to the BandPicture's foreign key
        history_year = HistoryYear(year=test_year,summary="Lots happened this year")
        history_year.save()
        picture.associated_history_year = history_year

        # Delete the picture and check to see if the HistoryYear still exists
        picture.delete()
        self.assertIs(HistoryYear.objects.filter(year=test_year).exists(),True)

    def test_band_picture_still_exists_after_deleting_history_year_its_related_to(self):
        test_caption = "Test caption"

        # Create BandPicture
        picture = create_band_picture(test_caption)
        picture.save()

        # Create the history year and add it to the BandPicture's foreign key
        history_year = HistoryYear(year=1990,summary="Lots happened this year")
        history_year.save()
        picture.associated_history_year=history_year

        # Delete the picture file
        picture.picture_file.delete()

        # Delete the history year and check to see if the BandPicture still exists
        self.assertIs(BandPicture.objects.filter(caption=test_caption).exists(),True)
