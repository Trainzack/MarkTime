from django.contrib import admin

from .models import EboardMember, HistoryYear, BandPicture, Recording, FAQ
# Register your models here.
admin.site.register(EboardMember)
admin.site.register(BandPicture)


class BandPictureInLine(admin.StackedInline):
    model = BandPicture
    extra = 0


class HistoryYearAdmin(admin.ModelAdmin):
    fields = ['year','summary']
    inlines = [BandPictureInLine]


admin.site.register(HistoryYear,HistoryYearAdmin)

admin.site.register(Recording)
admin.site.register(FAQ)