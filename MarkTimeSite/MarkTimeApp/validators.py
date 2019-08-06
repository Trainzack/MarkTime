import os
from django.core.exceptions import ValidationError


def validate_recording_file_extension(value):
    # [0] returns path+filename, [1] returns the extension
    extension = os.path.splitext(value.name)[1]

    # Add/Remove from the valid music file extensions as you see fit
    valid_extensions = ['.mp3','.ogg','.wave']
    if not extension.lower() in valid_extensions:
        raise ValidationError(u'Unsupported file extension')