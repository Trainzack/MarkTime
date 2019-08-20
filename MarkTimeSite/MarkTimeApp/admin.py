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


class HistoryYearAdmin(admin.ModelAdmin):
    fields = ['year','summary']
    inlines = [BandPictureInLine]


class BandPictureAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'picture_file', 'on_front_page', 'display_priority')
    list_editable = ('on_front_page', 'display_priority')
    list_filter = ('on_front_page',)


class EboardMemberAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'eboard_position')


class RecordingAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'in_books')
    list_editable = ('in_books',)
    list_filter = ('songname', 'in_books', 'date_recorded')


admin.site.register(BandPicture, BandPictureAdmin)
admin.site.register(EboardMember, EboardMemberAdmin)
admin.site.register(HistoryYear, HistoryYearAdmin)
admin.site.register(Recording, RecordingAdmin)