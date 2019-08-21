from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import EboardMember, BandPicture, FAQ, Recording, Announcement, HistoryYear

# Create your views here.


def index(request):
    front_page_pictures = BandPicture.objects.filter(on_front_page=True).order_by('-display_priority')
    announcements = Announcement.objects.all()
    context = {
        "page_pictures": front_page_pictures,
        "announcements": announcements,
        "in_home": True
    }
    return render(request, 'MarkTimeApp/index.html', context)
    # return HttpResponse("Dummy response for the index page")


def eboard_member(request, eboard_first_name, eboard_last_name):
    try:
        board_member = EboardMember.objects.get(first_name=eboard_first_name,last_name=eboard_last_name)
    except EboardMember.DoesNotExist:
        raise Http404("Eboard Member does not exist")
    response = "<h1>Eboard Member</h1>"
    response += "<h3>Name: " + str(board_member.first_name) + " " + str(board_member.last_name) + "</h3>"
    response += "<h3>Position: " + str(board_member.eboard_position) + "</h3>"
    response += "<img src=\"" + str(board_member.eboard_picture.picture_file.url) + "\"/>test"
    return HttpResponse(response)


def history_index(request):
    history_objects = HistoryYear.objects.all()
    context = {
        "history_objects": history_objects,
        "in_history": True
    }
    return render(request, 'MarkTimeApp/HistoryIndex.html', context)


def history_page(request, queried_year):
    try:
        history_object = HistoryYear.objects.get(year=queried_year)
    except HistoryYear.DoesNotExist:
        raise Http404("No record for the year " + str(queried_year))
    # If history_object exists build the context for the request
    context = {
        "history_object": history_object,
        # Get the bandpictures associated with this history year
        "page_pictures": history_object.bandpicture_set.all(),
        "in_history": True
    }
    return render(request, 'MarkTimeApp/HistoryPage.html', context)


def leadership(request):
    eboard_members = EboardMember.objects.all()
    context = {
        "eboard_members": eboard_members,
        "in_leadership": True
    }
    return render(request, 'MarkTimeApp/Leadership.html', context)


def faq(request):
    faq = FAQ.objects.all()
    context = {
        "FAQ": faq,
        "in_faq": True
    }
    return render(request, 'MarkTimeApp/FAQ.html',context)


def songs(request):
    recordings = Recording.objects.all()
    context = {
        "recordings": recordings,
        "in_songs": True
    }
    return render(request, 'MarkTimeApp/Songs.html',context)