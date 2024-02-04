from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404

# Create your views here.
def index(request):
    if request.method == "POST":
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        contact.name = name
        contact.email = email
        contact.subject = subject
        contact.save()
        return HttpResponse("<h3>Thank you!</h3>")
    
    main_list = Main.objects.latest('id')
    about_list = About.objects.latest('id')
    vision_list = Vision.objects.all()
    mission_list = Mission.objects.all()
    objective_list = Objective.objects.all()
    team_list = Team.objects.all()
    research_list = Research.objects.all()
    innovation_list = Innovation.objects.all()
    project_list = Project.objects.all()
    application_list = Application.objects.all()
    
    return render(request, 'main/index.html', {'main_list': main_list, 'about_list': about_list, 'vision_list': vision_list, 'mission_list': mission_list, 'objective_list': objective_list, 'team_list': team_list, 'research_list': research_list, 'innovation_list': innovation_list, 'project_list': project_list, 'application_list': application_list})

def casestudy(request):
   return render(request, 'main/casestudy.html')