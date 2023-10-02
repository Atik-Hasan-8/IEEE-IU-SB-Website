from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Event,Team,Upcomming_event,Contact,ExCom

def home_view(request):
    up_events=Upcomming_event.objects.all()
    ex_com_info=ExCom.objects.all()
    return render(request, 'index.html',{'up_events':up_events,'ex_com_info':ex_com_info})



def events_view(request):
    events = Event.objects.all()
    return render(request, 'events.html', {'events': events})

def about_view(request):
    return render(request, 'about.html')

def team_view(request):
    team_members = Team.objects.all()
    return render(request, 'teachers.html',{'team_members': team_members})

def blog_view(request):
    return render(request, 'blog.html')

# def contact_view(request):
#     return render(request, 'contact.html')

def event2_view(request):
    return render(request, 'events2.html')

def events_single_view(request):
    return render(request, 'events-single.html')

def events_single_1_view(request):
    return render(request, 'events-single-1.html')
def events_single_2_view(request):
    return render(request, 'events-single-2.html')

def events_single_3_view(request):
    return render(request, 'events-single-3.html')
def events_single_4_view(request):
    return render(request, 'events-single-4.html')

def events_single_5_view(request):
    return render(request, 'events-single-5.html')

def events_single_2_1_view(request):
    return render(request, 'event-signal-2_1.html')
def events_single_2_2_view(request):
    return render(request, 'event-signal-2_2.html')
def events_single_2_3_view(request):
    return render(request, 'event-signal-2_3.html')
def events_single_2_4_view(request):
    return render(request, 'event-signal-2_4.html')
def events_single_2_5_view(request):
    return render(request, 'event-signal-2_5.html')
def events_single_2_6_view(request):
    return render(request, 'event-signal-2_6.html')

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, subject=subject, phone=phone, message=message)
        contact.save()
        return render(request, 'contact.html')  # Assuming you have a success URL pattern named 'success'
    return render(request, 'contact.html')
