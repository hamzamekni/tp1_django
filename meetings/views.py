from django.shortcuts import get_object_or_404, render
from django.shortcuts import render, redirect
from .forms import MeetingForm
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

def add_meeting(request):
    if request.method == "POST":
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()  # Sauvegarde le meeting si le formulaire est valide
            return redirect('meetings_list_view')  # Redirige vers une liste de meetings ou une autre page après ajout
    else:
        form = MeetingForm()

    return render(request, 'new.html', {'form': form})

# Vue pour supprimer une réunion
def delete_meeting(request, id):
    meeting = get_object_or_404(Meeting, id=id) # Get the meeting by ID
    if request.method == "POST":
        meeting.delete()
        return redirect('meetings') # Redirect to the meetings list view after deletion
    return render(request, 'confirm_delete.html', {'meeting': meeting})
    # Render confirmation page

# Vue pour mettre à jour une réunion existante
def update_meeting(request, id):
    meeting = get_object_or_404(Meeting, id=id) # Récupérer la réunion par ID
    if request.method == "POST":
        form = MeetingForm(request.POST, instance=meeting) # Passer l'instance à mettre à jour
        if form.is_valid():
            form.save() # Sauvegarder les modifications
            return redirect('meetings') # Rediriger vers la liste des réunions
    else:
        form = MeetingForm(instance=meeting)  # Remplir le formulaire avec les données existantes
    return render(request, 'update_meeting.html', {'form': form}) #Rendre le template