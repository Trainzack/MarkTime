from django.contrib import admin
from django.contrib.auth.models import Group
from .models import EboardMember, HistoryYear, BandPicture, Recording, FAQ, Announcement
# Register your models here.
admin.site.unregister(Group)
admin.site.register(FAQ)
admin.site.register(Announcement)


class BandPictureInLine(admin.StackedInline):
    model = BandPicture
    extra = 0


# The different managers are written to display extra information in the admin pages
# list_display allow those attributes to be displayed on the model's admin page
# list_editable allow those attributes to be edited from the model's admin page
class HistoryYearAdmin(admin.ModelAdmin):
    fields = ['year', 'summary']
    inlines = [BandPictureInLine]


class BandPictureAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'picture_file', 'on_front_page', 'display_priority', 'associated_history_year')
    list_editable = ('on_front_page', 'display_priority', 'associated_history_year')
    list_filter = ('on_front_page',)


class EboardMemberAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'eboard_position')


class RecordingAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'in_books')
    list_editable = ('in_books',)
    list_filter = ('songname', 'in_books', 'date_recorded')


# Register model + manager for the admin site
admin.site.register(BandPicture, BandPictureAdmin)
admin.site.register(EboardMember, EboardMemberAdmin)
admin.site.register(HistoryYear, HistoryYearAdmin)
admin.site.register(Recording, RecordingAdmin)