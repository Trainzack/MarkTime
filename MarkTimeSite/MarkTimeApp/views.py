from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, Http404
from .models import EboardMember, BandPicture, FAQ, Song, Announcement, HistoryYear
from .forms import ContactForm, PerformanceRequestForm
from django.template.loader import render_to_string
from django.views.generic import ListView
from django.shortcuts import render_to_response
from django.template import RequestContext

# Create your views here.


def handler404(request, exception, template_name="MarkTimeApp/Custom404.html"):
    response = render_to_response('MarkTimeApp/Custom404.html')
    response.status_code = 404
    return response


def index(request):
    front_page_pictures = BandPicture.objects.filter(on_front_page=True).order_by('-display_priority')
    announcements = Announcement.objects.all()
    context = {
        "page_pictures": front_page_pictures,
        "announcements": announcements,
        "in_home": True
    }
    return render(request, 'MarkTimeApp/Index.html', context)
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
    history_objects = HistoryYear.objects.all().order_by('year')
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
        "in_history": True,
    }
    return render(request, 'MarkTimeApp/HistoryPage.html', context)


def picture_detail(request, pic_id):
    try:
        picture_object = BandPicture.objects.get(pk=pic_id)
    except BandPicture.DoesNotExist:
        raise Http404("No picture with that id exists")

    context={
        "picture_object": picture_object,
        "in_history": True
    }
    return render(request,'MarkTimeApp/PictureDetail.html', context)


def leadership(request):
    eboard_members = EboardMember.objects.all()
    context = {
        "eboard_members": eboard_members,
        "in_leadership": True
    }
    return render(request, 'MarkTimeApp/Leadership.html', context)


def faq(request):
    faq_objects = FAQ.objects.all()
    context = {
        "FAQ": faq_objects,
        "in_faq": True
    }
    return render(request, 'MarkTimeApp/FAQ.html',context)


def songs(request):
    recordings = Song.objects.all().order_by('song_name')
    context = {
        "recordings": recordings,
        "in_music": True
    }
    return render(request, 'MarkTimeApp/Music.html', context)


class RecordingListView(ListView):
    model = Song
    template_name = 'MarkTimeApp/Music.html'
    context_object_name = 'recordings'
    ordering = ['song_name']
    paginate_by = 5


def contact_us(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            # Create the subject of the email
            subject = form.cleaned_data['name'] + "'s Contact Form Response"

            # Use the form's responses to create context to pass into ContactResponse.txt
            email_message_context = {
                "name": form.cleaned_data['name'],
                "email": form.cleaned_data['email'],
                "instrument": form.cleaned_data['instrument'],
                "form_message": form.cleaned_data['message']
            }
            try:
                # Fills in the ContactResponse.txt template with the form's input and mail's it to the designated email
                send_mail(subject,
                          render_to_string('MarkTimeApp/ContactResponse.txt', email_message_context),
                          'christianmunoz110@gmail.com',
                          ['christianmunoz110@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('MarkTime-Index')
    return render(request, 'MarkTimeApp/ContactUs.html', {'form': form, 'in_contact': True})


def hire_us(request):
    if request.method == 'GET':
        form = PerformanceRequestForm()
    else:
        form = PerformanceRequestForm(request.POST)
        if form.is_valid():
            # Create the subject of the email
            subject = form.cleaned_data['name'] + " Requests a Pep Band Performance"

            # Use the form's responses to create context to pass into ContactResponse.txt
            email_message_context = {
                "name": form.cleaned_data['name'],
                "email": form.cleaned_data['email'],
                "event_name": form.cleaned_data['event_name'],
                "event_details": form.cleaned_data['event_details'],
            }
            try:
                # Fill in the ContactResponse.txt template with the generated
                # context and mail it to the designated email
                send_mail(subject,
                          render_to_string('MarkTimeApp/PerformanceRequestResponse.txt', email_message_context),
                          'christianmunoz110@gmail.com',
                          ['christianmunoz110@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('MarkTime-Index')
    return render(request, 'MarkTimeApp/ContactUsPerformance.html', {'form': form, 'in_contact_perf': True})