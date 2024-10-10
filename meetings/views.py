from django.shortcuts import get_object_or_404, render

from meetings.models import Meeting

# Create your views here.
def details(request, id):
    meeting = Meeting.objects.get(pk=id)
    return render(request, "meetings/detail.html", {"meeting": meeting})

def detaill(request, id):
    meeting = get_object_or_404(Meeting, id)
    return render(request, "meetings/detail.html", {"meeting": meeting})

def meetings_list_view(request):
    meetings = Meeting.objects.all()  # Get all meetings
    return render(request, 'meetings.html', {'meetings': meetings, })

def detail(request, id):
    meeting = get_object_or_404(Meeting, id=id)  
    return render(request, "details.html", {"meeting": meeting})