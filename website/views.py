from django.shortcuts import render
from meetings.models import Meeting

# Create your views here.
def home_view(request):
    context = {'nbre_meeting': Meeting.objects.count()}
    return render(request, "website/home.html", context)

def about_view(request):
    return render(request, "website/about.html")
