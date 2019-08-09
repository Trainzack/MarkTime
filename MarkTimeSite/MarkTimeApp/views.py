from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import EboardMember

# Create your views here.


def index(request):
    return render(request, 'MarkTimeApp/index.html')
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

def leadership(request):
    eboard_members = EboardMember.objects.all()
    context = {"eboard_members": eboard_members}
    return render(request, 'MarkTimeApp/Leadership.html', context)